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
    # PART 2 process
    task_sets
    def choose_framework(type_fw):
        pass
    
class EffortModel:
    # Section 33.7
    def cocomo():
        pass    

    def cocomo_2():
        pass
        
class MainEstimates:
    #step 3 : Predict the number of people who will be available to do the work is specified.
    def predicting_staffing_levels():
        number_of_available_people = 100

    #step 4: predicting_effort          
    def predicting_effort(models,size_work_products):
        #Estimation tools use one or more models (Section 33.7) 
        if models == cocomo:
        #models relate the size of the project to the effort required.
            if size_work_products.kloc > 100:
                return str(10)+'person-month'
        if models == cocomo_2:
            return 100
    
    # step 5 : Given the results of step 4, costs can be computed by allocating labor rates to the project activities noted in step 2. 
    def predicting_cost():
        import locale
        return locale.currency(188518982.18, grouping=True )

    # step 6 :  Predicting software schedules. 
    # When effort, staffing level, and project activities are known,
    def allocating_labor_across_activities():
        pass
    
    def effort_distribution():
        # chapter ?
        pass    

    def predicting_schedule():
        num_peoples = predicting_staffing_level
        allocating_labor_across_activities(num_peoples,effort_distribution)   

    def main():
        ProjectActivities.task_sets = ['planning','codings','deploy']

