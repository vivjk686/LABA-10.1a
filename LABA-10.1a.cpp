#include <iostream>
#include <iomanip>
#include <string>
#include <Windows.h>

using namespace std;

enum Specialnist { KN, INF, ME, FI, TN };
string specStr[] = { "Комп. науки", "Інформатика", "Мат. та ек.", "Фіз. та інф.", "Труд. навч." };

struct Student {
    string prizv;
    unsigned kurs;
    Specialnist spec;
    int fizyka;
    int matematyka;
    int informatyka;
};

void Create(Student* p, const int N);
void Print(const Student* p, const int N);
void CountPhysicsGrades(const Student* p, const int N, int& c5, int& c4, int& c3);
int CountPhysicsMathHighGrades(const Student* p, const int N);

int Utf8Len(const string& s) {
    int len = 0;
    for (unsigned char c : s) {
        if ((c & 0xC0) != 0x80) len++;
    }
    return len;
}

string PadRight(const string& s, int width) {
    int diff = width - Utf8Len(s);
    if (diff > 0) return s + string(diff, ' ');
    return s;
}

#ifndef UNIT_TEST
int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);

    int N;
    do {
        cout << "Введіть кількість студентів (N > 0): ";
        cin >> N;
        if (N <= 0) cout << "Помилка! Кількість має бути більшою за 0.\n";
    } while (N <= 0);

    Student* p = new Student[N];

    Create(p, N);
    Print(p, N);

    int c5 = 0, c4 = 0, c3 = 0;
    CountPhysicsGrades(p, N, c5, c4, c3);
    int highCount = CountPhysicsMathHighGrades(p, N);

    cout << "Кількість оцінок з фізики:" << endl;
    cout << "  «5» (відмінно):   " << c5 << endl;
    cout << "  «4» (добре):      " << c4 << endl;
    cout << "  «3» (задовільно): " << c3 << endl;
    cout << "Кількість студентів з оцінками «4» або «5» з фізики та математики: " << highCount << endl;

    delete[] p;
    return 0;
}
#endif

void Create(Student* p, const int N) {
    int ispec;
    for (int i = 0; i < N; i++) {
        cout << "Студент № " << i + 1 << ":" << endl;

        cout << " прізвище: ";
        cin >> ws;
        getline(cin, p[i].prizv);

        do {
            cout << " курс (1-6): ";
            cin >> p[i].kurs;
        } while (p[i].kurs < 1 || p[i].kurs > 6);

        do {
            cout << " спеціальність (0 - КН, 1 - ІНФ, 2 - МЕ, 3 - ФІ, 4 - ТН): ";
            cin >> ispec;
        } while (ispec < 0 || ispec > 4);
        p[i].spec = (Specialnist)ispec;

        do {
            cout << " оцінка з фізики (2-5): ";
            cin >> p[i].fizyka;
        } while (p[i].fizyka < 2 || p[i].fizyka > 5);

        do {
            cout << " оцінка з математики (2-5): ";
            cin >> p[i].matematyka;
        } while (p[i].matematyka < 2 || p[i].matematyka > 5);

        do {
            cout << " оцінка з інформатики (2-5): ";
            cin >> p[i].informatyka;
        } while (p[i].informatyka < 2 || p[i].informatyka > 5);

        cout << endl;
    }
}

void Print(const Student* p, const int N) {
    cout << "======================================================================" << endl;
    cout << "| № | Прізвище      | Курс | Спеціальність | Фіз. | Мат. | Інформ. |" << endl;
    cout << "----------------------------------------------------------------------" << endl;

    for (int i = 0; i < N; i++) {
        cout << "| " << setw(1) << right << i + 1 << " "
            << "| " << PadRight(p[i].prizv, 13)
            << " | " << setw(4) << right << p[i].kurs
            << " | " << PadRight(specStr[p[i].spec], 13)
            << " | " << setw(4) << right << p[i].fizyka
            << " | " << setw(4) << right << p[i].matematyka
            << " | " << setw(7) << right << p[i].informatyka << " |" << endl;
    }
    cout << "======================================================================" << endl << endl;
}

void CountPhysicsGrades(const Student* p, const int N, int& c5, int& c4, int& c3) {
    c5 = 0;
    c4 = 0;
    c3 = 0;
    for (int i = 0; i < N; i++) {
        if (p[i].fizyka == 5) c5++;
        else if (p[i].fizyka == 4) c4++;
        else if (p[i].fizyka == 3) c3++;
    }
}

int CountPhysicsMathHighGrades(const Student* p, const int N) {
    int count = 0;
    for (int i = 0; i < N; i++) {
        if ((p[i].fizyka == 4 || p[i].fizyka == 5) &&
            (p[i].matematyka == 4 || p[i].matematyka == 5)) {
            count++;
        }
    }
    return count;
}
