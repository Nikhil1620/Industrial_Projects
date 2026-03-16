StudyLedger-Java-Console-App

Technology: Java

Project Overview
The StudyLedger-Java-Console-App is a console-based Java application designed to
help students systematically log, track, summarize, and export their study activities.
It allows users to maintain daily study records, view summaries grouped by date or
subject, and export all logs into a CSV file for offline reference.
This project demonstrates practical usage of Java Collections, File I/O, and ObjectOriented Design in a real-world, utility-driven application.

Key Features
• Insert Study Log
◦ Record study sessions with date (auto-generated), subject, duration, and
description.
• Display Logs
◦ View all study logs currently stored in memory.
• Summary by Date
◦ Calculate & display total study hours grouped by date.
• Summary by Subject
◦ Calculate & display total study hours grouped by subject.
• Export to CSV
◦ Export all study logs into a CSV file (StudyLedger.csv) for offline
tracking.
• User-Friendly Console Menu
◦ Menu-driven interface with switch-case navigation for ease of use.

• Packages & APIs:
◦ java.util.* → Data structures (ArrayList, TreeMap), user input via Scanner.
◦ java.time.LocalDate → Auto-captures the current date for study logs.
◦ java.io.* → File handling and CSV export.

Project Flow
1. Launch the application → Main Menu displayed.
2. Choice 1: Insert new study log → User provides subject, duration, description → Date
auto-generated.
3. Choice 2: Display all study logs stored in memory.
4. Choice 3: Display summary grouped by date (total hours per day).
5. Choice 4: Display summary grouped by subject (total hours per subject).
6. Choice 5: Export all study logs to MarvellousStudy.csv.
7. Choice 6: Exit application.

Classes & Responsibilities
StudyLog
• Represents a single study session.
• Attributes: LocalDate date, String subject, double duration, String description.
• Methods: Constructor, getters, toString().
StudyTracker
• Manages all logs in memory.
• Attributes: ArrayList<StudyLog> database.
• Methods: InsertLog(), DisplayLog(), SummaryByDate(), SummaryBySubject(),
ExportCSV().
StudyTrackerApp (Main Class)
• Contains main() method.

• Handles menu-driven interface and user input.
• Calls appropriate methods from StudyTracker.

Example Usage (Console Flow)
====== StudyLedger-Java-Console-App ======
1. Insert Study Log
2. Display All Logs
3. Summary By Date
4. Summary By Subject
5. Export to CSV
6. Exit
Enter choice: 1
Enter Subject: Java Programming
Enter Duration (hours): 2.5
Enter Description: Practiced ArrayList and TreeMap
Study log added successfully for date: 2025-09-13
Sample Exported CSV (StudyLedger.csv)
Date,Subject,Duration,Description
2025-09-13,Java Programming,2.5,Practiced ArrayList and TreeMap
2025-09-13,Database,1.5,Revised SQL Joins

