def calc_safety_weight(yr3, yr2):
    if yr3 >= yr2:
        yr3 = yr3 * 60
        yr2 = yr2 * 40
    else:
        yr3 = yr3 *43
        yr2 = yr2 *57
    return (yr3 + yr2) / 100

def calc_yr_3_grd(mod, diss_grade, mod_num):
    grade = []
    product = 0
    factorx = 80/mod_num
    for i in range(mod_num):
        grade.append(mod[i] * factorx)
    for item in grade:
        product += item
    diss_grade = diss_grade * 40
    yr_grade = (product + diss_grade)/ 120
    return yr_grade

def main():
    YR_2_GRADE = float(input("Please enter yr2 grade as an integer. e.g. 70% = 70: "))
    print("Please enter 3rd year module grades as an integer. e.g. 70% = 70: ")
    mod_num = int(input("Number of modules: "))
    mod = []
    for i in range(mod_num):
        mod.append(float(input("module " + str(i+1) + " grade: ")))

    diss_grade = float(input("Project grade: "))
    yr_3 = calc_yr_3_grd(mod, diss_grade, mod_num)
    grade = calc_safety_weight(yr_3, YR_2_GRADE)
    print("your grade should be " + str(grade) + "%")
    input("Press enter to end program.")


if __name__ == '__main__':
    main()