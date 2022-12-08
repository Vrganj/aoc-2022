#include <iostream>

char mat[100][100];

char top[100][100];
char bottom[100][100];
char left[100][100];
char right[100][100];

bool visible(int i, int j) {
    if (i == 0 || i == 99 - 1 || j == 0 || j == 99 - 1) {
        return true;
    }

    char height = mat[i][j];

    return height > top[i - 1][j] ||
           height > bottom[i + 1][j] ||
           height > left[i][j - 1] ||
           height > right[i][j + 1];
}

int main() {
    for (int i = 0; i < 99; ++i) {
        for (int j = 0; j < 99; ++j) {
            std::cin >> mat[i][j];
        }
    }

    for (int j = 0; j < 99; ++j) {
        top[0][j] = mat[0][j];
        left[j][0] = mat[j][0];

        bottom[99-1][j] = mat[99-1][j];
        right[j][99-1] = mat[j][99-1];
    }

    for (int i = 1; i < 99; ++i) {
        for (int j = 0; j < 99; ++j) {
            top[i][j] = std::max(mat[i][j], top[i - 1][j]);
            bottom[99 - i - 1][j] = std::max(mat[99 - i - 1][j], bottom[99 - i][j]);
        }
    }

    for (int j = 1; j < 99; ++j) {
        for (int i = 0; i < 99; ++i) {
            left[i][j] = std::max(mat[i][j], left[i][j - 1]);
            right[i][99 - j - 1] = std::max(mat[i][99 - j - 1], right[i][99 - j]);
        }
    }

    int result = 0;

    for (int i = 0; i < 99; ++i) {
        for (int j = 0; j < 99; ++j) {
            result += visible(i, j);
        }
    }

    std::cout << result;

    return 0;
}
