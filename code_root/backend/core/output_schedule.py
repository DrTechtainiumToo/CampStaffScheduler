import datetime
from datetime import timezone
import logging
from code_root.backend.core.time_processes import get_current_week
from typing import Any
import json
from pathlib import Path

#NOTE colors are specified using a Html style #RRGGBB value.
#NOTE CASE text is set to capital by .upper() at the write function
#NOTE #Debuging REMEMBER to print it has to be assigned to each period and have the proper duration


class OutputSchedule(): 

    #TODO maybe later so can change settings while program runs from JSON file?
    output_settings_var: dict = {}
    
    def update_settings(self, new_settings):
        # Modifying the class variable
        OutputSchedule.output_settings_var = new_settings
        # Or equivalently, but less commonly used
        # self.__class__.output_settings_var = new_setting
        
    def __init__(self, day_time_slots_list, employee_list, employee_instances) -> None: #employee_list may be unessecarybut want to make sure in order same time, everytime.
        self.day_time_slots_list = day_time_slots_list
        self.length_time_slots = len(self.day_time_slots_list)
        self.employee_list = employee_list
        self.length_employee_list = len(employee_list)
        self.employee_instance = employee_instances
    
    def excel(self, employee_manager, task_manager, algo_run_time: float, GET_NEXT_DAY: bool, WEEK_COUNT_START_REF_DAY: str, UNAVAILABILITY_TASK: Any) -> None:
        import xlsxwriter
        
        from code_root.config.settings import excel_text_values_settings as etvs, excel_formatting_settings, task_format_dict, WEEK_COUNT_START_REF_DAY as ref_day
        print(ref_day)
        if etvs.get("date_output"):  
            if GET_NEXT_DAY:
                one_day = datetime.timedelta(days=1)
                current_day = datetime.datetime.now(timezone.utc).astimezone()
                day = (current_day + one_day).strftime("%A")
                #NOTE #%b - abrv month, %d -num date in month, %a - weekday abr name (depedns on region)
            else:
                day = datetime.datetime.now(timezone.utc).astimezone().strftime("%A")
                #NOTE WHY - strftime(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
                week_number_day: str = get_current_week(WEEK_COUNT_START_REF_DAY, GET_NEXT_DAY) + " " + day #FIXME idk why but WEEK_COUNT_START_REF_DAY acting up should work all right, no value, temp fix, PROB A FUNC ISSUE
        else:
            week_number_day = ""
            
        if etvs.get("quote_of_day"):
            quote_of_day = f'{etvs.get("quote_of_day", "No Quote of the day")}'
        else: 
            quote_of_day = f"No Quote of the day"
            
        file_title = f"{etvs.get("file_title", "SWAT Schedule")} {week_number_day}.xlsx"
        schedule_title = f'{etvs.get("schedule_title", "SWAT Schedule")}'
    
        
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(file_title)
        worksheet = workbook.add_worksheet(f"{schedule_title}{week_number_day}")
        worksheet.set_landscape()
        
        #Create formatting setting for stuff  - bc the values imported from settings dont have the add_format() method so i have to add it
        task_format = {}
        for key, fmt_settings in task_format_dict.items():
            task_format[key] = workbook.add_format(fmt_settings)
        
        efs = {}
        for key, fmt_settings in excel_formatting_settings.items():
            efs[key] = workbook.add_format(fmt_settings)
  
        #Write Date Label - Always in the top left corner
        worksheet.write(0, 0, week_number_day.upper(), efs.get("date_label_format"))
        
        # Column and Row indexes ----------------
        #NOTE - REMEMBER: Excel Rows/Columns are Zero based
        column_index = 1 #first column beyond the employee label column, aka the first column to put stuff into
        row_index = 4 #first row beyond the time slots label

        #Fill in corner gap between employees and schedule_title & time
        worksheet.write(1, 0, None, efs.get("corner_gap_fill_format"))
        worksheet.write(2, 0, None, efs.get("corner_gap_fill_format"))
        worksheet.write(3, 0, None, efs.get("corner_gap_fill_format"))
    
        # Write time headers
        time_slot_column_index = column_index
        for time_slot in self.day_time_slots_list:
            worksheet.write(row_index-1, time_slot_column_index, time_slot, efs.get("time_slot_format"))
            worksheet.set_column(time_slot_column_index-1, 70)
            time_slot_column_index += 1
        
        # Write employee names
        emp_row_index = row_index
        for employee in self.employee_list:
            worksheet.write(emp_row_index, 0, employee, efs.get("employee_format"))
            emp_row_index += 1
            
        # Fill in the data
        row = row_index        
        #NOTE WHY - cus all people have the same times in the day so can use for all employees. More efficent than in loop
        time_slots = self.day_time_slots_list
        
        #TODO ? WHY what if I just appended a None value to the next_slots list so that it technically has the same length but accurately represents that there is no next slot?
        next_time_slots = time_slots[1:] + [None] # NOTE WHY - Make lists same lenght, append None to represent that there is no next slot for the last item        
        
        def merge_unavailability_cells(UNAVAILABILITY_TASK, unavailbility_duration, column, row) -> tuple[int, bool]:
            #NOTE - WHY get() on next time slot to assign default value so that if last task of day, can pass elif statement, thus not needing an extra one for just end of the day situtations
            start_col = column - unavailbility_duration
            format = task_format.get(UNAVAILABILITY_TASK, task_format.get('Default'))  
            worksheet.merge_range(row, start_col, row, column-1, 'Unavailable', format)
            unavailbility_task_counter = 0
            unavailablity_sequence = False
            
            return unavailbility_task_counter, unavailablity_sequence
            
        #DONE functionize and modularize the loop
        for employee in self.employee_list:
            column = 1
            multi_period_task_counter = 0
            unavailbility_duration = 0
            unavailablity_sequence = False
            
            #NOTE if error check here, lol that rhymes. maybe give these props to output class, make simpler??[] 
            #print(list(employee_manager.employees[employee].assigned_to.values()))
            print(employee_manager.employees)
            
            tasks = list(employee_manager.employees[employee].assigned_to.values())
            for time_slot, next_time_slot, task in zip(time_slots, next_time_slots, tasks):
                format = task_format.get(task, task_format.get('Default'))
                
                if task == UNAVAILABILITY_TASK:
                    #part of sequence
                    if next_time_slot and employee_manager.employees[employee].assigned_to[next_time_slot] == UNAVAILABILITY_TASK:
                        unavailablity_sequence = True
                        unavailbility_duration +=1
                        column += 1
                        continue #skip rest of loop for efficency
                    #If sequence ends (bc no more unavails or end of day), or standalone unavailability, 
                    elif unavailablity_sequence or next_time_slot is None:
                        unavailbility_duration, unavailablity_sequence = merge_unavailability_cells(UNAVAILABILITY_TASK, unavailbility_duration, column, row)
                        column += 1
                        continue
                    else: #single unavailability
                        worksheet.write(row, column, task, format)
                        column += 1
                        continue
                
                elif task:
                    try:
                        duration = int(task_manager.tasks[task].duration) #why int = attr is assigned from csv sheet so need to convert it from string to int. #LEARNING use get get attr?? learn more. need to update my learning google doc. 
                    except ValueError:
                        duration: int = 1 #Fallback duration
                        logging.warning(f"At excel schedule output for {employee} for {time_slot} timeslot {task} was not able to get a value, assigned 1 as a default.")
                    
                    # If task spans multiple columns (x--->) 
                    if duration > 1:
                        multi_period_task_counter += 1
                        if multi_period_task_counter == duration:
                            start_col = column - (duration-1) #minus one bc duration count is inclusive, we have to account for timeslot we are in as part of it
                            worksheet.merge_range(row, start_col, row, column, task, format)
                            multi_period_task_counter = 0
                        column += 1
                    else: #If single duration
                        worksheet.write(row, column, task, format) #.get to prevent key error if i havent added a format for it, could i set it to None also? idk would have to read docs
                        column += 1
                        
                else: # If no task assigned, skip
                    worksheet.write(row, column, task) #just puts blank format
                    column += 1 
                    
            row += 1 # Move to the next row for the next employee
        
        #Write Title    #merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
        worksheet.merge_range(row_index-3, column_index,row_index-2,self.length_time_slots, schedule_title)
        worksheet.write(row_index-3, column_index, schedule_title, efs.get("title_format"))
        
        #Write Quote
        # Calculate the row to insert the quote based on the number of employees
        #NOTE WHY - row_index, row_index = the amount of gaps / rows between the first employee and top of the page. #Accounts for the rows that the date label, schedule_title, and timeslots take up so that the quote can be correctly positioned at the bottom of the page
        quote_row = self.length_employee_list + row_index 
        worksheet.merge_range(quote_row, 0, quote_row, self.
        length_time_slots, quote_of_day)
        
        # Apply the format to the merged cells with the quote
        worksheet.write(quote_row, 0, quote_of_day, efs.get("quote_format"))
        
        #Add a small row at the bottom with a footnote that gives me credit, plus runtime:      
        credit_note = f"Real Devious Task Scheduler designed by Yacht. Algo runtime: {round(algo_run_time, 3)} sec."        
        credit_row = self.length_employee_list + row_index + 1 # +1 to skip quote 
        worksheet.write(credit_row, 0, credit_note, efs.get("credit_note_format"))
        worksheet.merge_range(credit_row, 0, credit_row, 6, credit_note)        
        
        workbook.close()