def parse_input(input):
    report_list = []
    with open(input, 'r') as file:
        for line in file:
            report_list.append(list(map(int, line.split())))
    return report_list

def is_valid_diff(diff, is_increasing):
    return 1 <= abs(diff) <= 3 and ((is_increasing and diff > 0) or (not is_increasing and diff < 0))

def is_safe_report(report):
    if len(report) == 1:
        return True
        
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not is_valid_diff(diff, is_increasing):
            return False
    
    return True

def solve_part_one(report_list):
    num_safe_reports = 0
    for report in report_list:
        if is_safe_report(report):
            num_safe_reports += 1
    return num_safe_reports

def solve_part_two(report_list):
    num_safe_reports = 0
    for report in report_list:
        if is_safe_report(report):
            num_safe_reports += 1
        else:
            for i in range(len(report)):
                if is_safe_report(report[:i] + report[i+1:]):
                    num_safe_reports += 1
                    break
    return num_safe_reports

report_list = parse_input("./input.txt")

print(f"Part One: {solve_part_one(report_list)}")
print(f"Part Two: {solve_part_two(report_list)}")

