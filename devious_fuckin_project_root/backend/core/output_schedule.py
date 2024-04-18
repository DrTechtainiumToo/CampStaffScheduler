import datetime
from datetime import timezone

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
    
    def excel(self, employee_manager, task_manager) :
        import xlsxwriter

        #TODO MEDIUM - PRIORITY !! make system which able to input week, or starting week and will put what week it is, also let it choose between week or formal date         
        #TODO HARD - FOR FUTURE make formate setting system # FOURTH PRIORITY, for now just code into csv value - could do a bunch of pre made styles and have choose from them - hmm, but include a system that allows to make new styles easily
        #TODO MEDIUM HARD - figure out how to do up down stuff and diff style things SECOND PRIORITY
        #TODO make a standard font size and style for all tasks, make auto size and fit #THIRD PRIORITY
        #TODO make times_slot cubes a lil bigger, find out hwo sheets print and let that determine
        #TODO make quote autosize and fit
        #TODO make standard color fill for the borders and stuff
        #TODO MEDIUM - HARD (2-3horus) figure out prinitng paramteres and let it adjust box size based on that FIRST PRORITY
        #TODO make quote of the day prompt before all of this, and be able to turn on or off etc - make larger part of settings
        
        #NOTE REMEMBER to print it has to be assigned to each period and have the proper duration, will help with #Debuging
       
        #formatted_date_Month_Day = str(datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A, %m:%s")) #TODO LEARNING CONCEPT memorize reg-ex and the date-time exspressions
        formatted_date_month_day_weekday = datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A") #WHY - Str(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
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
        
        # Fill in the data
        row = row_index
        for employee in self.employee_list:
            column = 1
            multi_period_task_name_counter = 0
            for time_slot, task in employee_manager.employees[employee].assigned_to.items(): #NOTE if error check here, lol that rhymes. maybe give these props to output class, make simpler??[] 
                if task:
                    duration = int(task_manager.tasks[task].duration) #why int = attr is assigned from csv sheet so need to convert it from string to int. #LEARNING use get get attr?? learn more. need to update my learning google doc. 
                    #TODO error gaurding - WHAT if task doesn't have a duration, how should i guard against this error, what would ouput look like?
                    
                    # If task spans multiple columns
                    if duration > 1:
                        multi_period_task_name_counter += 1
                        if multi_period_task_name_counter == duration:
                            start_col = column - (duration-1) #minus one bc duration count is inclusive, we have to account for timeslot we are in as part of it
                            format = task_format.get(task, task_format.get('Default'))  
                            worksheet.merge_range(row, start_col, row, column, task, format)
                            multi_period_task_name_counter = 0
                        column += 1
                    else:
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
        workbook.close()
            
    def terminal():
        pass
