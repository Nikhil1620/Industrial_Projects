# Spring Boot CRUD Application with MongoDB

This repository contains a **Full Stack backend application** built using **Spring Boot** and **MongoDB**. The project demonstrates a clean and layered architecture for performing **CRUD (Create, Read, Update, Delete)** operations using RESTful APIs.

The application manages **Batch Entries**, including batch name, duration, and fees, and is designed following industry-standard best practices such as separation of concerns and dependency injection.

---

## 🚀 Technologies Used

- **Java**
- **Spring Boot**
- **Spring Data MongoDB**
- **MongoDB**
- **RESTful Web Services**
- **Maven**

---

## 📁 Project Structure

```
FullStack-Application
│
├── controller
│   └── BatchEntryController.java
│
├── service
│   └── BatchEntryService.java
│
├── repository
│   └── BatchEntryRepository.java
│
├── entity
│   └── BatchEntry.java
│
└── application.properties
```

Each package has a specific responsibility, making the application easy to maintain, scale, and test.

---

## 🧩 Package Description

### 1️⃣ Entity Layer (`entity`)

**File:** `BatchEntry.java`

- Represents the MongoDB document structure
- Maps Java objects to MongoDB collections
- Uses Spring Data annotations for persistence

**Key Annotations:**
- `@Document(collection = "batch_entry")` – Maps the class to a MongoDB collection
- `@Id` – Marks the primary key

This layer defines the data model used throughout the application.

---

### 2️⃣ Repository Layer (`repository`)

**File:** `BatchEntryRepository.java`

- Extends `MongoRepository`
- Handles all database-related operations
- Provides built-in CRUD methods without writing any implementation

**Key Interface:**
- `MongoRepository<BatchEntry, String>`

Spring Data MongoDB automatically generates implementations for common database operations.

---

### 3️⃣ Service Layer (`service`)

**File:** `BatchEntryService.java`

- Contains business logic
- Acts as a bridge between Controller and Repository layers
- Ensures clean separation of concerns

**Responsibilities:**
- Save batch details
- Fetch all batches
- Fetch batch by ID
- Update batch information
- Delete batch records

---

### 4️⃣ Controller Layer (`controller`)

**File:** `BatchEntryController.java`

- Exposes RESTful API endpoints
- Handles HTTP requests and responses
- Uses Spring MVC annotations

**Key Annotations:**
- `@RestController`
- `@RequestMapping`
- `@PostMapping`, `@GetMapping`, `@PutMapping`, `@DeleteMapping`

---

## 🔗 REST API Endpoints

| HTTP Method | Endpoint | Description |
|------------|----------|-------------|
| POST | `/batches` | Create a new batch |
| GET | `/batches` | Get all batches |
| GET | `/batches/{id}` | Get batch by ID |
| PUT | `/batches/{id}` | Update batch by ID |
| DELETE | `/batches/{id}` | Delete batch by ID |

---

## ⚙️ Configuration

Add the following configuration in `application.properties`:

```
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.database=MarvellousFullStack
```

Make sure MongoDB is running on your local system before starting the application.

---

## ▶️ How to Run the Application

1. Clone the repository
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Open the project in **IntelliJ IDEA / Eclipse / VS Code**

3. Ensure MongoDB is running
   ```
   mongod
   ```

4. Run the Spring Boot application

5. Test APIs using **Postman** or **curl**

---

## ✅ Features

- Clean layered architecture
- MongoDB integration using Spring Data
- RESTful CRUD operations
- Easy to extend and scalable
- Beginner-friendly and production-ready structure

---

## 📌 Future Enhancements

- Add validation using `@Valid`
- Exception handling with `@ControllerAdvice`
- Pagination and sorting
- Swagger/OpenAPI documentation
- Authentication & Authorization

---

## 👨‍💻 Author

Developed as part of a **Full Stack Spring Boot + MongoDB learning project**.

---

⭐ If you found this project helpful, feel free to star the repository!


