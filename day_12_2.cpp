#include <iostream>
#include <cstring>
#include <queue>

#define ROWS 41
#define COLS 113

char mat[ROWS][COLS];
int bio[ROWS][COLS];

int mx[4] { 0, 1, 0, -1 };
int my[4] { 1, 0, -1, 0 };

inline bool valid(int i, int j) {
    return i >= 0 && i < ROWS && j >= 0 && j < COLS;
}

int main(void) {
    memset(bio, -1, sizeof(bio));

    std::queue<std::pair<int, int>> queue;
    std::pair<int, int> end;

    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cin >> mat[i][j];

            if (mat[i][j] == 'S') {
                mat[i][j] = 'a';
            } else if (mat[i][j] == 'E') {
                mat[i][j] = 'z';
                end = { i, j };
            }

            if (mat[i][j] == 'a') {
                queue.push({ i, j });
                bio[i][j] = 0;
            }
        }
    }

    while (!queue.empty()) {
        std::pair<int, int> current = queue.front();
        queue.pop();

        int height = mat[current.first][current.second];

        for (int k = 0; k < 4; ++k) {
            int i = current.first + mx[k];
            int j = current.second + my[k];

            if (valid(i, j) && bio[i][j] == -1 && mat[i][j] <= height + 1) {
                bio[i][j] = bio[current.first][current.second] + 1;
                queue.push({ i, j });
            }
        }
    }

    std::cout << bio[end.first][end.second] << std::endl;

    return 0;
}
