#include <iostream>

char mat[100][100];

char top[100][100];
char bottom[100][100];
char left[100][100];
char right[100][100];

#define WIDTH 99
#define HEIGHT 99

bool visible(int i, int j) {
    if (i == 0 || i == HEIGHT - 1 || j == 0 || j == WIDTH - 1) {
        return true;
    }

    char height = mat[i][j];

    return height > top[i - 1][j] ||
           height > bottom[i + 1][j] ||
           height > left[i][j - 1] ||
           height > right[i][j + 1];
}

int main() {
    for (int i = 0; i < HEIGHT; ++i) {
        for (int j = 0; j < WIDTH; ++j) {
            std::cin >> mat[i][j];
        }
    }

    for (int j = 0; j < WIDTH; ++j) {
        top[0][j] = mat[0][j];
        bottom[HEIGHT-1][j] = mat[WIDTH-1][j];
    }

    for (int i = 0; i < HEIGHT; ++i) {
        left[i][0] = mat[i][0];
        right[i][WIDTH-1] = mat[i][WIDTH-1];
    }

    for (int i = 1; i < HEIGHT; ++i) {
        for (int j = 0; j < WIDTH; ++j) {
            top[i][j] = std::max(mat[i][j], top[i - 1][j]);
            bottom[HEIGHT - i - 1][j] = std::max(mat[HEIGHT - i - 1][j], bottom[HEIGHT - i][j]);
        }
    }

    for (int j = 1; j < WIDTH; ++j) {
        for (int i = 0; i < HEIGHT; ++i) {
            left[i][j] = std::max(mat[i][j], left[i][j - 1]);
            right[i][WIDTH - j - 1] = std::max(mat[i][WIDTH - j - 1], right[i][WIDTH - j]);
        }
    }

    int result = 0;

    for (int i = 0; i < HEIGHT; ++i) {
        for (int j = 0; j < WIDTH; ++j) {
            result += visible(i, j);
        }
    }

    std::cout << result;

    return 0;
}
