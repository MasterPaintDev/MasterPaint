#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_TITLE_LENGTH 100
#define MAX_AUTHOR_LENGTH 50

struct Book {
    char title[MAX_TITLE_LENGTH];
    char author[MAX_AUTHOR_LENGTH];
    int available;
};

struct Library {
    struct Book books[MAX_BOOKS];
    int count;
};

void initializeLibrary(struct Library *library) {
    library->count = 0;
}

void addBook(struct Library *library, const char *title, const char *author) {
    if (library->count < MAX_BOOKS) {
        struct Book newBook;
        strcpy(newBook.title, title);
        strcpy(newBook.author, author);
        newBook.available = 1; // Initially, book is available
        library->books[library->count++] = newBook;
        printf("Book added successfully.\n");
    } else {
        printf("Library is full. Cannot add more books.\n");
    }
}

void displayBooks(struct Library *library) {
    printf("Books in the library:\n");
    for (int i = 0; i < library->count; ++i) {
        printf("%d. Title: %s, Author: %s, Available: %s\n", i + 1, 
               library->books[i].title, library->books[i].author,
               library->books[i].available ? "Yes" : "No");
    }
}

int main() {
    struct Library library;
    initializeLibrary(&library);

    int choice;
    char title[MAX_TITLE_LENGTH], author[MAX_AUTHOR_LENGTH];

    do {
        printf("\nLibrary Management System\n");
        printf("1. Add a book\n");
        printf("2. Display all books\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter title of the book: ");
                scanf(" %[^\n]s", title);
                printf("Enter author of the book: ");
                scanf(" %[^\n]s", author);
                addBook(&library, title, author);
                break;
            case 2:
                displayBooks(&library);
                break;
            case 3:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}
