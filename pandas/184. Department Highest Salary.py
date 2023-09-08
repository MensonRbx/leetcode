import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame([],[],["Employee", "Salary", "Department"])
    departmentNames = list(department.sort_values(by = "id", ascending = True)["name"])

    groupByDepartment = employee.groupby("departmentId")
    
    for name, subGroup in groupByDepartment:
        subGroup = subGroup.sort_values(by = "salary", ascending = False)
        subGroup = subGroup[subGroup.salary == subGroup.salary.max()]
        del(subGroup["id"])
        
        subGroup.columns = ["Employee", "Salary", "_temp"]
        subGroup["Department"] = ["None" for i in range(subGroup.shape[0])]
        
        for index, value in enumerate(subGroup["_temp"]):
            subGroup.iloc[index, 3] = departmentNames[value-1]
        del(subGroup["_temp"])

        result = pd.merge_ordered(result, subGroup)
            
    result = result[["Department", "Employee", "Salary"]]   #change around for question to be correct
    return result

"""
Beats 5% of users in runtime. Too Bad!
"""
