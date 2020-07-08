#step 1: Sizing of project deliverables i.e work_products 
class ExternalRepresentation:
    screen = 10
    report = 10
class WorkProduct:
    kloc = 100
    function_point = 10
    page_documents = 100    
    ExternalRepresentation 

print(WorkProduct.kloc)
print(WorkProduct.ExternalRepresentation.screen)

# step 2 :  Selecting project activities
class ProjectActivities:
#     sss
    task_sets
    def choose_framework(type_fw):
        pass
    
class MainEstimates:
    #step 3 : Predict the number of people who will be available to do the work is specified.
    def predicting_staffing_levels:
        number_of_available_people = 100
#step 4: predicting_effort          
    def predicting_effort(models,size_work_products):
#         Estimation tools use one or more models (Section 33.7) 
        if models == 'cocomo':
#         models relate the size of the project to the effort required.
            if size_work_products.kloc > 100:
                return str(10)+'person-month'
        if models == 'cocomo II':
    
    def predicting_cost():
        import locale
        return locale.currency(188518982.18, grouping=True )
    
    def main:
        ProjectActivities.task_sets = ['planning','codings','deploy']

# 5. Predicting software cost. Given the results of step 4, costs can be computed by allocating labor rates to the project activities noted in step 2. 

# 6. Predicting software schedules. When effort, staffing level, and project activities are known,a draft schedule can be produced by allocating labor across software engineering activities based on recommended models for effort distribution discussed later in this chapter.