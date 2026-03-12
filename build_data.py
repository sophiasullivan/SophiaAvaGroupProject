from class_defs import SurveySubmission
from class_defs import StatVar

# Ava and Sophia
elementary = {"Total":StatVar(0.1375,0.2075,391), "Grade 5 Total":StatVar(-0.09, 0.345, 199), "Grade 5 Boys":StatVar(-0.01, 0.34, 102),"Grade 5 Girls":StatVar(0.71,-0.17,97), "Grade 1 Total":StatVar(-0.075, 0.33,192), "Grade 1 Boys":StatVar(-0.03,0.33,94), "Grade 1 Girls":StatVar(-0.12,0.33, 98)}

# Sophia
def attitude_calc(q1: str, q2: str, q3: str, q4: str, q5: str, q6: str, q7: str, q8: str, q9: str, q10: str, q11:str) -> float:
	attitude_count = 0
	if q1 == "True":
		attitude_count += 1
	else:
		attitude_count -= 1
	if q2 == "True":
		attitude_count += 1
	else:
		attitude_count -= 1
	if q3 == "True":
		attitude_count += 1.5
	else:
		attitude_count -= 1.5
	if q4 == "True":
		attitude_count -= 1.5
	else:
		attitude_count += 1.5
	if q5 == "True":
		attitude_count += 1.5
	else:
		attitude_count -= 1.5
	if q6 == "True":
		attitude_count += 1.5
	else:
		attitude_count -= 1.5
	if q7 == "True":
		attitude_count -= 1
	else:
		attitude_count += 1
	if q8 == "True":
		attitude_count -= 1
	else:
		attitude_count += 1
	if q9 == "True":
		attitude_count -= 1
	else:
		attitude_count += 1
	if q10 == "True":
		attitude_count += 1
	else:
		attitude_count -= 1
	if q11 == "True":
		attitude_count += 1.5
	else:
		attitude_count -= 1.5
	return round(attitude_count / 11, 2)

# Sophia
def getCPstudents() -> list[SurveySubmission]:
	all_submissions=[]
	cp_data = "cp_data.txt"
	with open(cp_data, "r") as f:
		lines = f.readlines()
	for line in lines:
		line = line.split(":")
		attitude_score = attitude_calc(line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
		newSubmission = SurveySubmission(line[0], line[1], line[2], line[3], attitude_score)
		all_submissions.append(newSubmission)
	return all_submissions