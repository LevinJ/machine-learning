# Import libraries
import numpy as np
import pandas as pd


class ExploreData:
    def __init__(self):
        # Read student data
        self.student_data = pd.read_csv("student-data.csv")
        print "Student data read successfully!"
        # Note: The last column 'passed' is the target/label, all other are feature columns
        return
    def showStats(self):
        # TODO: Compute desired values - replace each '?' with an appropriate expression/function call
        student_data = self.student_data
        n_students = student_data.shape[0]
        n_features = student_data.shape[1]-1
        n_passed = (student_data['passed'] == 'yes').sum()
        n_failed = (student_data['passed'] == 'no').sum()
        grad_rate = (n_passed/float(n_passed + n_failed)) * 100
        print "Total number of students: {}".format(n_students)
        print "Number of students who passed: {}".format(n_passed)
        print "Number of students who failed: {}".format(n_failed)
        print "Number of features: {}".format(n_features)
        print "Graduation rate of the class: {:.2f}%".format(grad_rate)
        return
    def run(self):
        self.showStats()
        return
    




if __name__ == "__main__":   
    obj= ExploreData()
    obj.run()