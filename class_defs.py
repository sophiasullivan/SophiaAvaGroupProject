# Sophia
class StatVar: #contains a demographic's statistical info
	def __init__(self, mean:float, sd:float, population:int):
		self.mean = mean
		self.sd = sd
		self.population = population
	def __repr__(self) -> str:
		return "Statistics[mean = {}, standard deviation = {}, population = {})".format(self.mean, self.sd, self.population)
	def __eq__(self, other) -> bool:
		return self is other or (self.mean == other.mean and self.sd == other.sd and self.population == other.population)

# Sophia
class SurveySubmission: #Cal Poly students
	def __init__(self, gender:str, ethnicity:str, college_yr:str, major:str, attitude:float):
		self.gender = gender
		self.ethnicity = ethnicity
		self.college_yr = college_yr
		self.major = major
		self.attitude = attitude
	def __repr__(self) -> str:
		return ("Survey Submission[gender = {}, ethnicity = {}, college year = {}, college of major = {}, math attitude = {}]"
			   .format(self.gender, self.ethnicity, self.college_yr, self.major, self.attitude))
	def __eq__(self, other) -> bool:
		return self is other or (self.gender == other.gender and self.ethnicity == other.ethnicity
								 and self.college_yr == other.college_yr and self.major == other.major
								 and self.attitude == other.attitude)
