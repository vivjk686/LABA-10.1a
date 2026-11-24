#include <iostream>
#include <iomanip>
#include <string>
#include <Windows.h>

using namespace std;

enum Specialnist {
    KOMP_NAUKY,
    INFORMATYKA,
    MAT_EKON,
    FIZ_INF,
    TRUD_NAVCH
};

const string specialnistStr[] = {
    "Комп’ютерні науки",
    "Інформатика",
    "Математика та економіка",
    "Фізика та інформатика",
    "Трудове навчання"
};

struct Student {
    string prizv;
    unsigned kurs;
    Specialnist spec;
    int physics;
    int math;
    int it;
};

void Create(Student* p, const int N);
void Print(const Student* p, const int N);
void CountPhysicsGrades(const Student* p, const int N, int& count5, int& count4, int& count3);
int CountPhysicsMathHighGrades(const Student* p, const int N);

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    int N;
    cout << "Введіть кількість студентів N: ";
    cin >> N;

    Student* p = new Student[N];

    Create(p, N);
    Print(p, N);

    int count5 = 0, count4 = 0, count3 = 0;
    CountPhysicsGrades(p, N, count5, count4, count3);

    cout << "Кількість оцінок з фізики:" << endl;
    cout << "  - «5» (відмінно):   " << count5 << endl;
    cout << "  - «4» (добре):      " << count4 << endl;
    cout << "  - «3» (задовільно): " << count3 << endl;
    cout << endl;

    int highGradesCount = CountPhysicsMathHighGrades(p, N);
    cout << "Кількість студентів, які отримали і з фізики, і з математики оцінки «4» або «5»: "
         << highGradesCount << endl;

    delete[] p;
    return 0;
}

void Create(Student* p, const int N)
{
    int ispec;
    for (int i = 0; i < N; i++)
    {
        cout << "Студент № " << i + 1 << ":" << endl;
        cin.get();
        cin.sync();

        cout << "  прізвище: "; getline(cin, p[i].prizv);
        cout << "  курс: "; cin >> p[i].kurs;
        cout << "  спеціальність (0 - Комп’ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): ";
        cin >> ispec;
        p[i].spec = (Specialnist)ispec;
        cout << "  оцінка з фізики: "; cin >> p[i].physics;
        cout << "  оцінка з математики: "; cin >> p[i].math;
        cout << "  оцінка з інформатики: "; cin >> p[i].it;
        cout << endl;
    }
}

void Print(const Student* p, const int N)
{
    cout << "==========================================================================================" << endl;
    cout << "| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Інформатика |" << endl;
    cout << "------------------------------------------------------------------------------------------" << endl;
    for (int i = 0; i < N; i++)
    {
        cout << "| " << setw(3) << right << i + 1 << " ";
        cout << "| " << setw(14) << left << p[i].prizv << " ";
        cout << "| " << setw(4) << right << p[i].kurs << " ";
        cout << "| " << setw(23) << left << specialnistStr[p[i].spec] << " ";
        cout << "| " << setw(6) << right << p[i].physics << " ";
        cout << "| " << setw(10) << right << p[i].math << " ";
        cout << "| " << setw(11) << right << p[i].it << " |" << endl;
    }
    cout << "==========================================================================================" << endl;
    cout << endl;
}

void CountPhysicsGrades(const Student* p, const int N, int& count5, int& count4, int& count3)
{
    count5 = 0;
    count4 = 0;
    count3 = 0;
    for (int i = 0; i < N; i++)
    {
        if (p[i].physics == 5)
            count5++;
        else if (p[i].physics == 4)
            count4++;
        else if (p[i].physics == 3)
            count3++;
    }
}

int CountPhysicsMathHighGrades(const Student* p, const int N)
{
    int count = 0;
    for (int i = 0; i < N; i++)
    {
        if ((p[i].physics == 4 || p[i].physics == 5) &&
            (p[i].math == 4 || p[i].math == 5))
        {
            count++;
        }
    }
    return count;
}
