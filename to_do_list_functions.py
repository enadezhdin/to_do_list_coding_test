# to-do-list list of functions
import datetime


def initialize_list():
    '''Function initializes empty python dictionary as a to do list'''
    to_do_list={}
    return to_do_list

def to_do_list_main(to_do_list):
    '''Function processes input from user and select what task to perform''' 
    task = user_interface()
    if task == 'v':
        view_list(to_do_list)
    elif task == 'a':
        add_task(to_do_list)
    elif task == 'c':
        mark_as_complete(to_do_list)
    elif task == 'd':
        delete_from_list(to_do_list)
    else:
        print('Sorry, please select input from the list')


def user_interface():
    '''function gets input from user from provided list of options:
    A - add new task to the list
    D - delete task from the list
    C - mark task as complete
    V - view whole list'''
    print('Hello! Welcome to to-do-list. Please, define what you want to do.', '\n', 'To add task, enter A','\n', 'To mark as complete, enter C','\n', 'To delete task, enter D', '\n', 'To view the whole list, enter V')
    task = input().lower().strip()
    return task


def view_list(to_do_list):
    '''function print out contains of to do list'''
    print('Task \t\t\t\tEntered date\tDue date\tStatus')
    for key in to_do_list.keys():
        print('{0:30}\t{1:10}\t{2:14}\t{3}'.format(key, to_do_list[key][1], to_do_list[key][2], to_do_list[key][0]))


def add_task(to_do_list):
    '''function addes and process new items to the to do list'''
    print ('Please enter new task', '\n')
    new_task = input().strip()
    if len(new_task) > 30:
        print ('Please use up to 30 symbols for task')                         #to avoid braking table shape, length of task should be <=30
    if new_task!='':                                                           #check that input is not empty
        print('You also can input due date for the task \nEnter date in form DD.MM.YYYY or press Enter to skip')
        while True:                                                            #startin while cycle to allow multiple inputs if user make an error
            due_date = input()
            if due_date != '':
                try:                                                           #handling exception to avoid error message if data format wrong
                    due_date_true = str(datetime.datetime.strptime(due_date, '%d.%m.%Y'))[:10]   #selecting only first 10 symbols of the output to only get date (not date and time)
                    break
                except (ValueError):
                    print('Plese enter date in correct format - DD.MM.YYYY')

            else:
                due_date = 'not specified'
                break
    completness = 'not complete'                                               #default value for new task - not complete
    input_date = str(datetime.date.today())                                    #generates timestamp when task was eneterd into the list
    to_do_list[new_task] = [completness, input_date, due_date]
    return to_do_list


def mark_as_complete(to_do_list):
    '''function allows to mark particular task from the list as complete'''
    print ('Please select from the list the task you want mark as complete.')
    view_list (to_do_list)                                                      #using view_list() function to print out contains of the list
    completed_task = input().strip()
    if completed_task in to_do_list.keys():                                    #cheking if the entered task in the list
        to_do_list[completed_task][0] = 'complete'
        print ('Here the list of completed tasks so far:')
        print ('Task \t\t\t\tEntered date\tDue date\tStatus')
        for compl_key in to_do_list.keys():
            if to_do_list[compl_key][0] == 'complete':
                print('{0:30}\t{1:10}\t{2:14}\t{3}'.format(compl_key, to_do_list[compl_key][1], to_do_list[compl_key][2], to_do_list[compl_key][0]))
    else:
        print ('Sorry, the task you entered is not in the current list')
    return to_do_list



def delete_from_list(to_do_list):
    '''finction deletes selected task from the list'''
    print ('Please select from the list the task you want to delete.')
    view_list (to_do_list)                                                     #using view_list() function to print out contains of the list
    task_to_delete = input().strip()
    if task_to_delete in to_do_list.keys():                                    #checking if the task to delete in the current list 
        del to_do_list[task_to_delete]
        print ('Task', task_to_delete, 'sucesfully deleted')
    else:
        print('Sorry, the task you want to delete is not in the current list')
    return to_do_list




