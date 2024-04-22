import datetime
from datetime import timezone
import logging
from config.settings import UNAVAILABILITY_TASK, GET_NEXT_DAY
from backend.core.time_processes import get_current_week

class OutputSchedule(): 
    #TODO FIGURE OUT LATER

    output_settings_var = {}
    excel_formatting_settings = {}

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
    
    def core_tabular_output_logic():
        #core logic from how task outputted for all tables, only difference is file type and formatting. 
        #Thus easy to change lgoic for all output forms rather than have to do each one.
        pass
    
    def csv():
        pass
    
    def excel(self, employee_manager, task_manager, algo_run_time: float) :
        import xlsxwriter

        #TODO MEDIUM - PRIORITY !! make system which able to input week, or starting week and will put what week it is, also let it choose between week or formal date         
        #TODO HARD - FOR FUTURE make formate setting system # FOURTH PRIORITY, for now just code into csv value - could do a bunch of pre made styles and have choose from them - hmm, but include a system that allows to make new styles easily
        #TODO MEDIUM HARD - figure out how to do up down stuff and diff style things SECOND PRIORITY
        #DONE make a standard font size and style for all tasks, make auto size and fit #THIRD PRIORITY
        #TODO make times_slot cubes a lil bigger, find out how sheets print and let that determine
        #TODO make standard color fill for the borders and stuff, #can use settings sutf esle #TODO make defaults for reset and stuff.
        #TODO MEDIUM - HARD (2-3horus) figure out prinitng paramteres and let it adjust box size based on that FIRST PRORITY
        
        #NOTE #Debuging REMEMBER to print it has to be assigned to each period and have the proper duration
       
        if GET_NEXT_DAY:
            one_day = datetime.timedelta(days=1)
            current_day = datetime.datetime.now(timezone.utc).astimezone()
            formatted_date_month_day_weekday = (current_day + one_day).strftime("%A") #%b %d,
        else:
            formatted_date_month_day_weekday = datetime.datetime.now(timezone.utc).astimezone().strftime(" &A") #WHY - Str(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
            #WHY - strftime(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
            
        file_title = f"SWAT Schedule {formatted_date_month_day_weekday}.xlsx" #%b - abrv month, %d -num date in month, %a - weekday abr name (depedns on region)
        title = 'SCHEDULE'
        quote_of_day = "Quote of the day"
        
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(file_title)
        worksheet = workbook.add_worksheet(f"SWAT Schedule {formatted_date_month_day_weekday}")
        
        # Define formats
        schedule_axis_fill_color ='#404040'
        schedule_axis_label_color ='#FFFFFF'
        tasks_and_employee_cell_height = ''
        #task_default_font_color ='#333333'
        
        #colors are specified using a Html style #RRGGBB value.
        date_label_format = workbook.add_format({ #CASE text is set to capital by .upper() at the write function
            'bold': True, 
            'align': 'left',
            'valign': 'vcenter',
            #'fg_color': '#FFD3D3D3',
            'font_size': 10,
            'border': 1
        })
        title_format = workbook.add_format({ #TODO UPDATE
            'bold': True, 
            'align': 'center',
            'valign': 'vcenter',
            'font_color': schedule_axis_label_color,
            'fg_color': schedule_axis_fill_color,
            'font_size': 30,
            #'border': 1
        })
        time_slot_format = workbook.add_format({
            'bold': True, 
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D3D3D3',
            'font_size': 12,
            'border': 1
        })
        employee_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': schedule_axis_fill_color,
            'font_color': schedule_axis_label_color
            #TODO make it shrink the text to auto fit
        })
        corner_gap_fill_format = workbook.add_format({
            'fg_color': schedule_axis_fill_color
        })
        quote_format = workbook.add_format({ #TODO UPDATE??
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': schedule_axis_fill_color,  # Background color
            'font_color': schedule_axis_label_color,  # Font color
            'font_size': 30,
            'bold': True,
            #'border': 1
        })
        #make a .CSV and autoconver values, also find work around for KSWAT and such.
        
        #TODO put these in settings file, no magic shit
        task_format = {
        'Default' : workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'SERVE': workbook.add_format({
            'bg_color': '#FFFFCC',
            'border': 1
        }),
        'HALF STAFF': workbook.add_format({
            'bg_color': '#C6EFCE',
            'border': 1
        }),
        'SEE R00SKI': workbook.add_format({
            'bg_color': '#FFD9B3',
            'border': 1
        }),
        'SEE JESUS': workbook.add_format({
            'bg_color': '#FFF2CC',
            'border': 1
        }),
        'MAIL': workbook.add_format({
            'bg_color': '#DDEBF7',
            'border': 1
        }),
        'DISH': workbook.add_format({
            'bg_color': '#FFEB9C',
            'border': 1
        }),
        'PLAYTIME/OFF': workbook.add_format({
            'bg_color': '#B6D7A8',
            'border': 1
        }),
        'SEE SLIPS': workbook.add_format({
            'bg_color': '#D9D9D9',
            'border': 1
        }),
        'BALLOONS': workbook.add_format({
            'bg_color': '#EAD1DC',
            'border': 1
        }),
        'PHONES': workbook.add_format({
            'bg_color': '#DBDBDB',
            'border': 1
        }),
        'CAMP STORE': workbook.add_format({
            'bg_color': '#C9DAF8',
            'border': 1
        }),
        'PIZZA': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'DH': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'WATER RUN': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'BALLOONS': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'FLAG DOWN': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'SEE EAGLE': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'FLAG UP': workbook.add_format({
            'bg_color': '#F4CCCC',
            'border': 1
        }),
        'KSWAT1' : workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#FFB6C1',
            'font_color': '#333333',
            'border': 1
        }),
        'KSWAT2' : workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#FFB6C1',
        'font_color': '#333333',
        'border': 1
        }),
        'KSWAT3' : workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#FFB6C1',
        'font_color': '#333333',
        'border': 1
        }),
        UNAVAILABILITY_TASK : workbook.add_format({ #unavailable
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#8B0000',
        'font_color': '#000000',
        'border': 1
        })
        }

        #Write Date Label - Always in the top left corner
        worksheet.write(0, 0, formatted_date_month_day_weekday.upper(), date_label_format)
        
        # Column and Row indexes ----------------
        #NOTE - REMEMBER: Excel Rows/Columns are Zero based
        column_index = 1 #first column beyond the employee label column, aka the first column to put stuff into
        row_index = 4 #first row beyond the time slots label

        #Fill in corner gap between employees and title & time
        worksheet.write(1, 0, None, corner_gap_fill_format,)
        worksheet.write(2, 0, None, corner_gap_fill_format,)
        worksheet.write(3, 0, None, corner_gap_fill_format,)
    
        # Write time headers
        time_slot_column_index = column_index
        for time_slot in self.day_time_slots_list:
            worksheet.write(row_index-1, time_slot_column_index, time_slot, time_slot_format)
            worksheet.set_column(time_slot_column_index-1, 70) #NOTE #TODO adjs height, find way to make consistent for all cells, read docs
            time_slot_column_index += 1
        
        # Write employee names
        emp_row_index = row_index
        for employee in self.employee_list:
            worksheet.write(emp_row_index, 0, employee, employee_format)
            emp_row_index += 1

        #TODO make tasks check thier future unavailbility
        #Put in programming notes
         
        #Pre-checks: Move simpler, more frequently true conditions to the beginning of your conditional checks.
        
        # Fill in the data
        row = row_index        
        #cus all people have the same times in the day so can use for all employees. More efficent than in loop
        time_slots = self.day_time_slots_list
        #WHY what if I just appended a None value to the next_slots list so that it technically has the same length but accurately represents that there is no next slot?
        next_time_slots = time_slots[1:] + [None] # Make lists same lenght, append None to represent that there is no next slot for the last item        
        
        #TODO functionize and modularize the loop
        for employee in self.employee_list:
            column = 1
            multi_period_task_counter = 0
            unavailbility_task_counter = 0
            unavailablity_sequence = False
            
            #for time_slot, task in employee_manager.employees[employee].assigned_to.items(): #NOTE if error check here, lol that rhymes. maybe give these props to output class, make simpler??[] 
            tasks = list(employee_manager.employees[employee].assigned_to.values())
            for time_slot, next_time_slot, task in zip(time_slots, next_time_slots, tasks):
                if task:
                    if task == 0: # 0 = unvailability
                        duration: int = 1
                    else:
                        try:
                            duration = int(task_manager.tasks[task].duration) #why int = attr is assigned from csv sheet so need to convert it from string to int. #LEARNING use get get attr?? learn more. need to update my learning google doc. 
                        except ValueError:
                            duration: int = 1 #Fallback duration
                            logging.warning(f"At excel schedule output for {employee} for {time_slot} timeslot {task} was not able to get a value, assigned 1 as a default.")
                    
                    if task == UNAVAILABILITY_TASK:
                        unavailablity_sequence = True
                        unavailbility_task_counter +=1
                        format = task_format.get(task, task_format.get('Default'))
                        worksheet.write(row, column, task, format)
                        column += 1
                        continue
                    elif unavailablity_sequence and next_time_slot is not None and employee_manager.employees[employee].assigned_to.get(next_time_slot, 0) != UNAVAILABILITY_TASK: #merge all contiguous unavailable time slots into a single merged cell                                                #One ahead of last unavailble task, current task is a regular one, so have to go back
                        #get() on next time slot to assign default value so that if last task of day, can pass elif statement, thus not needing an extra one for just end of the day situtations
                        start_col = column - unavailbility_task_counter
                        format = task_format.get(0, task_format.get('Default'))  
                        worksheet.merge_range(row, start_col, row, column-1, 'Unavailable', format)
                        unavailbility_task_counter = 0
                        unavailablity_sequence = False
                    elif unavailablity_sequence and next_time_slot is None: #is last time_slot and need to merge 
                        start_col = column - unavailbility_task_counter
                        format = task_format.get(0, task_format.get('Default'))  
                        worksheet.merge_range(row, start_col, row, column-1, 'Unavailable', format)
                        unavailbility_task_counter = 0
                        unavailablity_sequence = False
                        
                    # If task spans multiple columns (x--->) 
                    if duration > 1:
                        multi_period_task_counter += 1
                        if multi_period_task_counter == duration:
                            start_col = column - (duration-1) #minus one bc duration count is inclusive, we have to account for timeslot we are in as part of it
                            format = task_format.get(task, task_format.get('Default'))  
                            worksheet.merge_range(row, start_col, row, column, task, format)
                            multi_period_task_counter = 0
                        column += 1
                    else: #If single duration
                        format = task_format.get(task, task_format.get('Default'))  #bc wont take a list type thing in the ar
                        worksheet.write(row, column, task, format) #.get to prevent key error if i havent added a format for it, could i set it to None also? idk would have to read docs
                        column += 1
                else:
                    worksheet.write(row, column, task) #just puts blank
                    column += 1  # Skip if no task
            row += 1
        
        #Write Title    #merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
        worksheet.merge_range(row_index-3, column_index,row_index-2,self.length_time_slots, title)
        worksheet.write(row_index-3, column_index, title, title_format)
        
        #Write Quote
        # Calculate the row to insert the quote based on the number of employees
        quote_row = self.length_employee_list + row_index # WHY +row_index, row_index = the amount of gaps / rows between the first employee and top of the page. #Accounts for the rows that the date label, title, and timeslots take up so that the quote can be correctly positioned at the bottom of the page
        worksheet.merge_range(quote_row, 0, quote_row, self.length_time_slots, quote_of_day)
        # Apply the format to the merged cells with the quote
        worksheet.write(quote_row, 0, quote_of_day, quote_format)
        
        #Write footnote
        #Add a small row at the bottom with a footnote that gives me credit, plus runtime:
        credit_note_format = workbook.add_format({
            'bold': True, 
            'align': 'left',
            'valign': 'vcenter',
            #'fg_color': '#FFD3D3D3',
            'font_size': 8,
            'border': 1
        })
        
        credit_note = f"Real Devious Task Scheduler designed by Yacht. Algo runtime: {round(algo_run_time, 3)} sec."
        #help my name jeff, i am trapped inside the program, someone please help me escape.
        credit_row = self.length_employee_list + row_index + 1 # +1 to skip quote 
        worksheet.write(credit_row, 0, credit_note, credit_note_format)
        worksheet.merge_range(credit_row, 0, credit_row, 6, credit_note)
        #worksheet.merge_range(first_row, first_col, last_row, last_col, data, cell_format=None)
       
        #Final joke note under credit footnote:
        
        
        workbook.close()