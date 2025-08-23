# Yoobee College Use Case Design

---

##  1. Project Scope

Yoobee College offers a variety of courses for students, including **Design**, **Technology**, **Animation**, **Film**, and **Marketing**.  
To support the management of academic data, a centralized **database system** is needed.  
This system will store and organize information about **students**, **tutors**, **classes**, and **enrollments**.

**Goals:**
- Clearly represent relationships between entities  
- Improve data accessibility  
- Reduce errors caused by manual record-keeping  

---

## 2. Actors

| Actor           | Description                                        |
|------------------|----------------------------------------------------|
| **Administrator** | Manages system data (courses, tutors, students)   |
| **Tutor**         | Views course/class info, assists with assignments |
| **Student**       | Views available courses and enrolls               |

---

## 3. Use Cases

| Use Case                     | Actor          |
|------------------------------|----------------|
| Add course                   | Administrator  |
| Add tutor                    | Administrator  |
| View tutor                   | Administrator  |
| Delete tutor                 | Administrator  |
| Add student                  | Administrator  |
| View student                 | Administrator  |
| Choose the class for course | Tutor          |
| View all courses             | Student        |

---

## 4. Use Case Diagrams

### First Diagram – Administrator Use Cases

![FirstUML](act1%20UML.png)

### Second Diagram – Tutor & Student Use Cases

![SecUML](act1%20UML-2.png)

---

## 5. Use Case Descriptions (Brief)

| Use Case                     | Brief Description                                   |
|------------------------------|-----------------------------------------------------|
| **Add course**               | Administrator adds course to the system            |
| **Add tutor**                | Administrator assigns tutor to a class             |
| **View tutor**               | Administrator views the tutor(s) of a class        |
| **Delete tutor**             | Administrator removes tutor from a class           |
| **Add student**              | Administrator adds student to a class              |
| **View student**             | Administrator views student(s) in a class          |
| **Choose the class for course** | Tutor selects class assigned to a course     |
| **View all courses**         | Student browses all available courses              |

---

