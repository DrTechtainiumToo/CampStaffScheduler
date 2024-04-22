import datetime
from datetime import timezone
import xlsxwriter

#NOTE REMEMBER to print it has to be assigned to each period and have the proper duration, will help with #Debuging
assigned = {"7:00am": "KSWAT1", "7:45am": "KSWAT1", "9:15am": "KSWAT1", "9:50am": "KSWAT1", "10:00am": "Unavailable", "11:00am": None, "11:45am": "Something", '1:45pm': 'Something'}
task_durs = {"KSWAT1": 4, "HALFSTAFF": 1, "Something": 2}
employee_list = ["Huey", "Granddad", "Wuncler"]

def excel(dayList, dayName):
    #TODO MEDIUM - PRIORITY !! make system which able to input week, or starting week and will put what week it is, also let it choose between week or formal date 
    
    formatted_date_Month_Day = str(datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A, %m:%s")) #TODO LEARNING CONCEPT memorize reg-ex and the date-time exspressions
    formatted_date_month_day_weekday = datetime.datetime.now(timezone.utc).astimezone().strftime("%b %d, %A") #WHY - Str(), because the xlsxwriter cannot take anyhting but a string or float, so cant assign to a cell. So make sure it is a str.
    file_title = f"TYPE 2 {formatted_date_month_day_weekday}.xlsx" #%b - abrv month, %d -num date in month, %a - weekday abr name (depedns on region)
    title = 'SCHEDULE'
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(file_title)
    worksheet = workbook.add_worksheet(f"SWAT Schedule {formatted_date_month_day_weekday}")
    
    # Define formats
    
    #TODO HARD - FOR FUTURE make formate setting system # FOURTH PRIORITY, for now just code into csv value - could do a bunch of pre made styles and have choose from them - hmm, but include a system that allows to make new styles easily
    #TODO MEDIUM HARD - figure out how to do up down stuff and diff style things SECOND PRIORITY
    
    #TODO make a standard font size and style for all tasks, make auto size and fit #THIRD PRIORITY
    #TODO make times_slot cubes a lil bigger, find out hwo sheets print and let that determine
    #TODO make quote autosize and fit
    #TOOD make standard color fill for the borders and stuff
    
    #TODO MEDIUM - HARD (2-3horus) figure out prinitng paramteres and let it adjust box size based on that FIRST PRORITY
    
    schedule_axis_fill_color ='#404040'
    schedule_axis_label_color ='#FFFFFF'
    tasks_and_employee_cell_height = ''
    #ask_default_color ='#333333'
    date_label_format = workbook.add_format({ #CASE text is set to capital by .upper() at the write function
        'bold': True, 
        'align': 'left',
        'valign': 'vcenter',
        #'fg_color': '#FFD3D3D3',
        'font_size': 10,
        'border': 1
    })
    #colors are specified using a Html style #RRGGBB value.
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
    KSWAT_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#FFB6C1',
        'font_color': '#333333',
        'border': 1
    })
    #maybe a class for task formats???? hmm hard code for now then think if want to input with task or want a seperate control.

    #Write Date Label - Always in the top left corner
    worksheet.write(0, 0, formatted_date_month_day_weekday.upper(), date_label_format)
    
    # Column and Row indexes ----------------
    #NOTE***REMEMBER: Excel Rows/Columns are Zero based
    column_index = 1 #first column beyond the employee label column, aka the first column to put stuff into
    row_index = 4 #first row beyond the time slots label

    #Fill in corner gap between employees and title & time
    worksheet.write(1, 0, None, corner_gap_fill_format,)
    worksheet.write(2, 0, None, corner_gap_fill_format,)
    worksheet.write(3, 0, None, corner_gap_fill_format,)
 
    # Write time headers
    time_slot_column_index = column_index
    for time_slot in dayList:
        worksheet.write(row_index-1, time_slot_column_index, time_slot, time_slot_format)
        worksheet.set_column(time_slot_column_index-1, 70) #NOTE #TODO adjs height, find way to make consistent for all cells, read docs
        time_slot_column_index += 1
    
    # Write employee names
    emp_row_index = row_index
    for employee in employee_list:
        worksheet.write(emp_row_index, 0, employee, employee_format)
        emp_row_index += 1
    
    # Fill in the data
    row = row_index
    for employee in employee_list:
        column = 1
        multi_period_task_name_counter = 0
        for time_slot, task in assigned.items():
            if task:
                duration = task_durs.get(task, 1)
                # If task spans multiple columns
                if duration > 1:
                    multi_period_task_name_counter += 1
                    if multi_period_task_name_counter == duration:
                        start_col = column - (duration-1) #minus one bc duration count is inclusive, we have to account for timeslot we are in as part of it
                        worksheet.merge_range(row, start_col, row, column, task, KSWAT_format)
                        #worksheet.write(row, column, task)
                        multi_period_task_name_counter = 0
                    column += 1
                else:
                    worksheet.write(row, column, task)
                    column += 1
            else:
                worksheet.write(row, column, task)
                column += 1  # Skip if no task
        row += 1
    
    #Write Title    #merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
    worksheet.merge_range(row_index-3, column_index,row_index-2,column_index+(len(dayList)), title)
    worksheet.write(row_index-3, column_index, title, title_format)
    
    #Write Quote
    # Define the quote of the day
    quote_of_day = "Quote of the day"
    # Calculate the row to insert the quote based on the number of employees
    quote_row = len(employee_list) + row_index # WHY +row_index, row_index = the amount of gaps / rows between the first employee and top of the page. #Accounts for the rows that the date label, title, and timeslots take up so that the quote can be correctly positioned at the bottom of the page
    # Merge cells for the quote
    worksheet.merge_range(quote_row, 0, quote_row, len(dayList), quote_of_day)
    # Apply the format to the merged cells with the quote
    worksheet.write(quote_row, 0, quote_of_day, quote_format)
    workbook.close()

dayNameA = "Monday"
List_day = ['7:00am','7:45am','9:15am','9:50am','10:00am','11:00am','11:45am','1:45pm','2:45pm']

excel(List_day, dayNameA)
