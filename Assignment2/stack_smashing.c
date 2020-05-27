#include <stdio.h>
#include <string.h>

void temp_func(char *buf) {
    char temp_str[5];
    for (int i = 0; i < strlen(buf); i++) {
        temp_str[i] = buf[i];
    }
}

int main() {
    char str[10];
    for (int i = 0; i < 10; i++) {
        str[i] = 'A' + i;
    }
    temp_func(str);
    return 0;
}
