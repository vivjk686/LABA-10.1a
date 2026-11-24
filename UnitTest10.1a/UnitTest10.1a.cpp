#include "pch.h"
#include "CppUnitTest.h"
#include "../LABA-10.1a/student.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest101a
{
    TEST_CLASS(UnitTest101a)
    {
    public:
        TEST_METHOD(TestCountPhysicsGrades)
        {
            const int N = 4;
            Student students[N] = {
                { "Коваленко", 1, KOMP_NAUKY, 5, 5, 5 },
                { "Іваненко",  2, INFORMATYKA, 4, 4, 4 },
                { "Петренко",  1, MAT_EKON,    3, 5, 4 },
                { "Сидоренко", 3, FIZ_INF,     5, 3, 5 }
            };

            int c5 = 0, c4 = 0, c3 = 0;
            CountPhysicsGrades(students, N, c5, c4, c3);

            Assert::AreEqual(2, c5);
            Assert::AreEqual(1, c4);
            Assert::AreEqual(1, c3);
        }

        TEST_METHOD(TestCountPhysicsMathHighGrades)
        {
            const int N = 4;
            Student students[N] = {
                { "Коваленко", 1, KOMP_NAUKY, 5, 5, 5 }, // 5, 5 -> YES
                { "Іваненко",  2, INFORMATYKA, 4, 4, 4 }, // 4, 4 -> YES
                { "Петренко",  1, MAT_EKON,    3, 5, 4 }, // 3, 5 -> NO (physics is 3)
                { "Сидоренко", 3, FIZ_INF,     5, 3, 5 }  // 5, 3 -> NO (math is 3)
            };

            int highCount = CountPhysicsMathHighGrades(students, N);
            Assert::AreEqual(2, highCount);
        }
    };
}
