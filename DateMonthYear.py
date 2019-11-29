import re
def DateMonthYear(d):
	date_reg_exp = '^((0)[1-9]|(1)[0-2])(\/)([0-2][0-9]|(3)[0-1])(\/)((1)[8-9]), ([2-9]|(1)[0-2]|(1))(\:)([0-5][0-9]) ([P][M]|[A][M]) -'
	find = re.match(date_reg_exp, d)
	if find:
		return True
	return False
