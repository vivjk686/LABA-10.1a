#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

enum Specialnist { KN, INF, ME, FI, TN };
string specStr[] = { "Komp. nauky", "Informatyka", "Mat. ta ek.", "Fiz. ta inf.", "Trud. navch." };

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

#ifndef UNIT_TEST
int main() {
    int N;
    do {
        cout << "Vvedit kilkist studentiv (N > 0): ";
        cin >> N;
        if (N <= 0) cout << "Pomylka! Kilkist maye buty bilshoyu za 0.\n";
    } while (N <= 0);

    Student* p = new Student[N];

    Create(p, N);
    Print(p, N);

    int c5 = 0, c4 = 0, c3 = 0;
    CountPhysicsGrades(p, N, c5, c4, c3);
    int highCount = CountPhysicsMathHighGrades(p, N);

    cout << "Kilkist otsinok z fizyky:" << endl;
    cout << "  \"5\" (vidminno):   " << c5 << endl;
    cout << "  \"4\" (dobre):      " << c4 << endl;
    cout << "  \"3\" (zadovilno):  " << c3 << endl;
    cout << "Kilkist studentiv z otsinkamy \"4\" abo \"5\" z fizyky ta matematyky: " << highCount << endl;

    delete[] p;
    return 0;
}
#endif

void Create(Student* p, const int N) {
    int ispec;
    for (int i = 0; i < N; i++) {
        cout << "Student # " << i + 1 << ":" << endl;

        cout << " prizvyshche: ";
        cin >> ws;
        getline(cin, p[i].prizv);

        do {
            cout << " kurs (1-6): ";
            cin >> p[i].kurs;
        } while (p[i].kurs < 1 || p[i].kurs > 6);

        do {
            cout << " spetsialnist (0 - KN, 1 - INF, 2 - ME, 3 - FI, 4 - TN): ";
            cin >> ispec;
        } while (ispec < 0 || ispec > 4);
        p[i].spec = (Specialnist)ispec;

        do {
            cout << " otsinka z fizyky (2-5): ";
            cin >> p[i].fizyka;
        } while (p[i].fizyka < 2 || p[i].fizyka > 5);

        do {
            cout << " otsinka z matematyky (2-5): ";
            cin >> p[i].matematyka;
        } while (p[i].matematyka < 2 || p[i].matematyka > 5);

        do {
            cout << " otsinka z informatyky (2-5): ";
            cin >> p[i].informatyka;
        } while (p[i].informatyka < 2 || p[i].informatyka > 5);

        cout << endl;
    }
}

void Print(const Student* p, const int N) {
    cout << "=====================================================================" << endl;
    cout << "| # |   Prizvyshche | Kurs | Spetsialnist  | Fiz. | Mat. | Inform. |" << endl;
    cout << "---------------------------------------------------------------------" << endl;

    for (int i = 0; i < N; i++) {
        cout << "| " << setw(1) << right << i + 1 << " "
            << "| " << setw(13) << left << p[i].prizv
            << " | " << setw(4) << right << p[i].kurs
            << " | " << setw(13) << left << specStr[p[i].spec]
            << " | " << setw(4) << right << p[i].fizyka
            << " | " << setw(4) << right << p[i].matematyka
            << " | " << setw(7) << right << p[i].informatyka << " |" << endl;
    }
    cout << "=====================================================================" << endl << endl;
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
