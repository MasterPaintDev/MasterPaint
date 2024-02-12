#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Book {
private:
    string title;
    string author;
    bool available;

public:
    Book(string title, string author) : title(title), author(author), available(true) {}

    const string& getTitle() const {
        return title;
    }

    const string& getAuthor() const {
        return author;
    }

    bool isAvailable() const {
        return available;
    }

    void setAvailable(bool available) {
        this->available = available;
    }
};

class Library {
private:
    vector<Book> books;

public:
    void addBook(const string& title, const string& author) {
        books.emplace_back(title, author);
        cout << "Book added successfully." << endl;
    }

    void displayBooks() {
        cout << "Books in the library:" << endl;
        for (size_t i = 0; i < books.size(); ++i) {
            cout << i + 1 << ". Title: " << books[i].getTitle() 
                 << ", Author: " << books[i].getAuthor() 
                 << ", Available: " << (books[i].isAvailable() ? "Yes" : "No") << endl;
        }
    }
};

int main() {
    Library library;

    int choice;
    string title, author;

    do {
        cout << "\nLibrary Management System" << endl;
        cout << "1. Add a book" << endl;
        cout << "2. Display all books" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter title of the book: ";
                cin.ignore();
                getline(cin, title);
                cout << "Enter author of the book: ";
                getline(cin, author);
                library.addBook(title, author);
                break;
            case 2:
                library.displayBooks();
                break;
            case 3:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 3);

    return 0;
}
