import class_defs
import build_data
import math
from typing import Optional

# Ava and Sophia
grade_list=["First year undergraduate student","Second year undergraduate student","Third year undergraduate student","Fourth year undergraduate student"]
ethnicity_list=["White","Asian","Hispanic/Latinx","Two or more races/ethnicities","American/Alaskan Native"]
gender_list=["Woman","Man"]
major_list=["Bailey College of Science and Mathematics (COSAM)","College of Agriculture, Food, and Environmental Sciences (CAFES)",
            "College of Architecture and Environmental Design (CAED)","College of Engineering (CENG)",
            "College of Liberal Arts (CLA)","Orfalea College of Business (OCOB)"]

# Ava
def filter_by_ethnicity(lst:list[class_defs.SurveySubmission],key:str) -> list:
    filtered_lst=[]
    for student in lst:
        if student.ethnicity == key:
            filtered_lst.append(student)
    print("Filtered List:", filtered_lst)
    return filtered_lst

# Ava
def filter_by_gender(lst:list[class_defs.SurveySubmission],key:str) -> list:
    filtered_lst=[]
    for student in lst:
        if student.gender == key:
            filtered_lst.append(student)
    print("Filtered List:", filtered_lst)
    return filtered_lst

# Ava
def filter_by_major(lst:list[class_defs.SurveySubmission],key:str) -> list:
    filtered_lst=[]
    for student in lst:
        if student.major== key:
            filtered_lst.append(student)
    print("Filtered List:", filtered_lst)
    return filtered_lst

# Ava
def filter_by_grade(lst:list[class_defs.SurveySubmission],key:str):
    filtered_lst = []
    for student in lst:
        if student.college_yr == key:
            filtered_lst.append(student)
    print("Filtered List:", filtered_lst)
    return filtered_lst

# Sophia and Ava
def get_mean(lst:list[class_defs.SurveySubmission], key) -> Optional[float]:
    try:
        if key in gender_list:
            filtered_list = filter_by_gender(lst, key)
            attitude_count = 0
            for i in lst:
                attitude_count += i.attitude
            filter_pop=len(filtered_list)
            total_mean = round(attitude_count / filter_pop,2)
            print(key, "'s mean math attitude = ", total_mean)
            return (total_mean)
        if key in major_list:
            filtered_list =filter_by_major(lst,key)
            attitude_count = 0
            for i in filtered_list:
                attitude_count += i.attitude
            filter_pop = len(filtered_list)
            total_mean = round(attitude_count / filter_pop,2)
            print(key, "'s mean math attitude = ", total_mean)
            return (total_mean)
        if key in ethnicity_list:
            filtered_list = filter_by_ethnicity(lst, key)
            attitude_count = 0
            for i in filtered_list:
                attitude_count += i.attitude
            filter_pop = len(filtered_list)
            total_mean = round(attitude_count / filter_pop,2)
            print(key, "'s mean math attitude = ", total_mean)
            return (total_mean)
        if key in grade_list:
            filtered_list = filter_by_grade(lst, key)
            attitude_count = 0
            for i in filtered_list:
                attitude_count += i.attitude
            filter_pop = len(filtered_list)
            total_mean = round(attitude_count / filter_pop,2)
            print(key, "'s mean math attitude = ", total_mean)
            return total_mean
        if key not in gender_list and key not in major_list and key not in ethnicity_list and key not in grade_list:
            print("Error: key provided does not exist")
            return None
        else:
            print("Error: mean cannot be calculated from provided list")
            return None
    except ZeroDivisionError as e:
        print(e)
        print("Error: mean cannot be calculated from provided list of length 0")
        return None

# Sophia
def get_sd(lst: list[class_defs.SurveySubmission], key: str) -> Optional[float]:
    if len(lst) > 0:
        if key in gender_list:
            filtered_list = filter_by_gender(lst, key)
        elif key in major_list:
            filtered_list = filter_by_major(lst, key)
        elif key in ethnicity_list:
            filtered_list = filter_by_ethnicity(lst, key)
        elif key in grade_list:
            filtered_list = filter_by_grade(lst, key)
        else:
            print("Error: provided key does not exist")
            return None
        pop = len(filtered_list)
        if pop < 2:
            print("Standard deviation between less than 2 individuals is 0.0")
            return 0.0
        mean = get_mean(filtered_list, key)
        sd = 0
        for person in filtered_list:
            sd += (person.attitude - mean) ** 2
        sd = math.sqrt(sd / (pop - 1))
        print(key, "'s standard deviation math attitude = ", sd)
        return round(sd, 2)
    else:
        print("Error: standard deviation cannot be calculated from provided list of length 0")
        return None

# Sophia and Ava
def get_Statdata(sub:list[class_defs.SurveySubmission],key:str) -> Optional[class_defs.StatVar]:
    if len(sub) > 0:
        if key in ethnicity_list:
            lst = filter_by_ethnicity(sub,key)
            pop = len(lst)
            mean = get_mean(lst, key)
            sd = get_sd(lst, key)
            stats = class_defs.StatVar(mean, sd, pop)
            print("Statistics: mean = ", mean, " standard deviation = ", sd, " population size = ", pop)
            return stats
        if key in gender_list:
            lst=filter_by_gender(sub,key)
            pop = len(lst)
            mean = get_mean(lst, key)
            sd = get_sd(lst, key)
            stats = class_defs.StatVar(mean, sd, pop)
            print("Statistics: mean = ", mean, " standard deviation = ", sd, " population size = ", pop)
            return stats
        if key in grade_list:
            lst=filter_by_grade(sub,key)
            pop = len(lst)
            mean = get_mean(lst, key)
            sd = get_sd(lst, key)
            stats = class_defs.StatVar(mean, sd, pop)
            print("Statistics: mean = ", mean, " standard deviation = ", sd, " population size = ", pop)
            return stats
        if key in major_list:
            lst=filter_by_major(sub,key)
            pop = len(lst)
            mean = get_mean(lst, key)
            sd = get_sd(lst, key)
            stats = class_defs.StatVar(mean, sd, pop)
            print("Statistics: mean = ", mean, " standard deviation = ", sd, " population size = ", pop)
            return stats
        else:
            print("Error: provided key does not exist")
            return None
    else:
        print("Error: mean and standard deviation statistics cannot be calculated from provided list of length 0")
        return None

# Ava
def compare_mean(obj1:str, obj2:str, lst:list[class_defs.SurveySubmission]) -> Optional[float]:
    if len(lst) > 0:
        if obj1 in build_data.elementary:
            obj1_statvar= build_data.elementary[obj1]
        elif obj1 in grade_list or obj1 in major_list or obj1 in gender_list or obj1 in ethnicity_list:
            obj1_statvar = get_Statdata(lst, obj1)
        else:
            print("Error: provided key for object 1 does not exist")
            return None
        if obj2 in build_data.elementary:
            obj2_statvar= build_data.elementary[obj2]
        elif obj2 in grade_list or obj2 in major_list or obj2 in ethnicity_list or obj2 in gender_list:
            obj2_statvar = get_Statdata(lst ,obj2)
        else:
            print("Error: provided key for object 2 does not exist")
            return None
    else:
        print("Error: means cannot be calculated from provided list of length 0")
        return None
    if obj1_statvar.mean>obj2_statvar.mean:
        print (obj1," mean math attitude is greater than ",obj2," mean math attitude, ",obj1_statvar.mean," > ",obj2_statvar.mean)
        return obj1_statvar.mean
    elif obj2_statvar.mean>obj1_statvar.mean:
        print (obj2," mean math attitude is greater than ",obj1," mean math attitude, ",obj2_statvar.mean," > ",obj1_statvar.mean)
        return obj2_statvar.mean
    else:
        print (obj1," mean math attitude is equal to ",obj2," mean math attitude, ",obj1_statvar.mean," = ",obj2_statvar.mean)
        return obj1_statvar.mean

# Ava
def compare_sd(obj1, obj2, lst:list[class_defs.SurveySubmission]) -> Optional[float]:
    if len(lst) > 0:
        if obj1 in build_data.elementary:
            obj1_statvar= build_data.elementary[obj1]
        elif obj1 in grade_list or obj1 in major_list or obj1 in gender_list or obj1 in ethnicity_list:
            obj1_statvar = get_Statdata(lst, obj1)
        else:
            print("Error: provided key for object 1 does not exist")
            return None
        if obj2 in build_data.elementary:
            obj2_statvar= build_data.elementary[obj2]
        elif obj2 in grade_list or obj2 in major_list or obj2 in ethnicity_list or obj2 in gender_list:
            obj2_statvar = get_Statdata(lst ,obj2)
        else:
            print("Error: provided key for object 2 does not exist")
            return None
    else:
        print("Error: standard deviations cannot be calculated from provided list of length 0")
        return None
    if obj1_statvar.sd > obj2_statvar.sd:
        print(obj1," standard deviation math attitude is greater than ",obj2," standard deviation math attitude, ",obj1_statvar.sd," > ",obj2_statvar.sd)
        return obj1_statvar.sd
    elif obj2_statvar.sd > obj1_statvar.sd:
        print(obj2, " standard deviation math attitude is greater than ", obj1, " standard deviation math attitude, ", obj2_statvar.sd, " > ", obj1_statvar.sd)
        return obj2_statvar.sd
    else:
        print(obj1, " standard deviation math attitude is equal to ", obj2, " standard deviation math attitude, ", obj1_statvar.sd, " = ", obj2_statvar.sd)
        return obj1_statvar.sd
