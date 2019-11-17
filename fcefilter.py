import pandas as pd

def filterCourses(courses, ratingLimit):
    fces = pd.read_csv('fce.csv')
    filteredCourses = dict()
    for course in courses:
        course = course.replace('-', '')
        courseRows = fces.loc[fces['Course ID'] == course]
        professors = courseRows['Name'].unique()

        for professor in professors:
            professorCourseRows = courseRows.loc[fces['Name'] == professor]
            meanOverallRating = professorCourseRows['Overall course rate'].mean()
            meanOverallRating = round(meanOverallRating, 2)
            print(course, professor, meanOverallRating)
            if meanOverallRating >= ratingLimit:
                filteredCourses[course] = filteredCourses.get(course, []) + [(professor, meanOverallRating)]
    return filteredCourses

# Ex. Courses
courses = ['15-112', '21127']
ratingLimit = 4
print(filterCourses(courses, ratingLimit))