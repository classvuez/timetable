# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    TITLE = (
        ('Dr', 'Dr'),
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms')
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user_profile_id = models.AutoField(db_column='user_profileID', primary_key=True)
    initials = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=3, blank=True, null=True, choices=TITLE)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER)
    auth_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.auth_user.first_name + " " + self.auth_user.last_name

    class Meta:
        managed = True
        db_table = 'user_profile'


class Administrator(models.Model):
    admin_id = models.AutoField(db_column='adminID', primary_key=True)
    user_profile_user_profile_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE,
                                                     db_column='user_profile_user_profileID')

    def __str__(self):
        return self.auth_user.first_name + " " + self.auth_user.last_name

    class Meta:
        managed = False
        db_table = 'administrator'


class Attendance(models.Model):
    attendance_id = models.AutoField(db_column='attendanceID', primary_key=True)
    student_stud_num = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_studNum')
    class_class_id = models.ForeignKey('Class', on_delete=models.CASCADE, db_column='class_classID')

    class Meta:
        managed = True
        db_table = 'attendance'


class Class(models.Model):
    CLASS_STATUS = (
        ('L', 'Late'),
        ('C', 'Cancelled'),
        ('O', 'Ongoing')
    )

    class_id = models.AutoField(db_column='classID', primary_key=True)
    weekday = models.CharField(db_column='weekDay', max_length=9)
    start = models.TimeField()
    end = models.TimeField()
    class_status = models.CharField(db_column='classStatus', max_length=1, choices=CLASS_STATUS)
    subject_sub_code = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subject_subCode')
    lecturer_staff_num = models.ForeignKey('Lecturer', on_delete=models.CASCADE, db_column='lecturer_staffNum')

    class Meta:
        managed = True
        db_table = 'class'


class Consultation(models.Model):
    BOOK_CONSULTATION = (
        ('Y', 'Yes'),
        ('C', 'Cancel')
    )

    CONSULTATION_STATUS = (
        ('A', 'Available'),
        ('U', 'Unavailable'),
        ('O', 'Out')
    )

    consultation_id = models.AutoField(db_column='consultationID', primary_key=True)
    weekday = models.CharField(db_column='weekDay', max_length=9, blank=True, null=True)
    start = models.TimeField()
    end = models.TimeField(blank=True, null=True)
    book_consultation = models.CharField(db_column='bookConsultation',max_length=1, choices=BOOK_CONSULTATION)
    topic = models.CharField(max_length=500)
    consultation_status = models.CharField(db_column='consultationStatus', max_length=1, blank=True, null=True,
                                           choices=CONSULTATION_STATUS)
    subject_sub_code = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subject_subCode')
    lecturer_staff_num = models.ForeignKey('Lecturer', on_delete=models.CASCADE, db_column='lecturer_staffNum')
    student_stud_num = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_studNum')

    class Meta:
        managed = True
        db_table = 'consultation'


class Course(models.Model):
    course_code = models.CharField(db_column='courseCode', primary_key=True, max_length=6)
    course_name = models.CharField(db_column='courseName', max_length=80, blank=True, null=True)
    year_offered = models.IntegerField(db_column='yearOffered')
    department_department_id = models.ForeignKey('Department', on_delete=models.CASCADE,
                                                 db_column='department_departmentID')

    def __str__(self):
        return self.course_name

    class Meta:
        managed = True
        db_table = 'course'


class Department(models.Model):
    department_id = models.AutoField(db_column='departmentID', primary_key=True)
    dept_name = models.CharField(db_column='deptName', max_length=50, blank=True, null=True)
    faculty_faculty_id = models.ForeignKey('Faculty', on_delete=models.CASCADE, db_column='faculty_facultyID')

    def __str__(self):
        return self.dept_name

    class Meta:
        managed = True
        db_table = 'department'


class Enrollment(models.Model):
    enrollment_id = models.AutoField(db_column='enrollmentID', primary_key=True)
    year = models.IntegerField()
    current_semester = models.IntegerField(db_column='currentSemester')
    subject_sub_code = models.ForeignKey('Subject', on_delete=models.CASCADE, db_column='subject_subCode')
    course_course_code = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_courseCode')

    class Meta:
        managed = True
        db_table = 'enrollment'


class Faculty(models.Model):
    faculty_id = models.AutoField(db_column='facultyID', primary_key=True)
    faculty_name = models.CharField(db_column='facultyName', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.faculty_name

    class Meta:
        managed = True
        db_table = 'faculty'


class Lecturer(models.Model):
    staff_num = models.IntegerField(db_column='staffNum', primary_key=True)
    office_nr = models.CharField(db_column='officeNr', max_length=30, blank=True, null=True)
    phone_nr = models.CharField(db_column='phoneNr', max_length=20, blank=True, null=True)
    department_department_id = models.ForeignKey(Department, on_delete=models.CASCADE,
                                                 db_column='department_departmentID')
    user_profile_user_profile_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE,
                                                     db_column='user_profile_user_profileID')
    course_course_code = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_courseCode')

    def __str__(self):
        return self.user_profile_user_profile_id.auth_user.first_name + " " + \
               self.user_profile_user_profile_id.auth_user.last_name

    class Meta:
        managed = True
        db_table = 'lecturer'


class Student(models.Model):
    stud_num = models.IntegerField(db_column='studNum', primary_key=True)
    year = models.IntegerField()
    bus_reg = models.IntegerField(db_column='busReg')
    t_cs = models.IntegerField(db_column='T&Cs')
    course_course_code = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_courseCode')
    user_profile_user_profile_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE,
                                                     db_column='user_profile_user_profileID')

    def __str__(self):
        return self.user_profile_user_profile_id.auth_user.first_name + " " + \
               self.user_profile_user_profile_id.auth_user.last_name

    class Meta:
        managed = True
        db_table = 'student'


class Subject(models.Model):
    sub_code = models.CharField(db_column='subCode', primary_key=True, max_length=7)
    sub_name = models.CharField(db_column='subName',max_length=80, blank=True, null=True)
    year = models.IntegerField()
    semester = models.IntegerField()
    lecturer_staff_num = models.ForeignKey(Lecturer, on_delete=models.CASCADE, db_column='lecturer_staffNum')

    def __str__(self):
        return self.sub_code

    class Meta:
        managed = True
        db_table = 'subject'


class Venue(models.Model):
    venue_id = models.AutoField(db_column='venueID', primary_key=True)
    building = models.IntegerField()
    class_nr = models.CharField(db_column='classNr', max_length=5)
    class_class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_classID')

    def __str__(self):
        return str(self.building) + "-" + str(self.class_nr)

    class Meta:
        managed = True
        db_table = 'venue'
