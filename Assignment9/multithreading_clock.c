#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>


pthread_mutex_t lock;
int seconds, minutes, hours;

void* print_hour(void* pString) {
    pthread_mutex_lock(&lock);
    if(minutes > 59){
        hours++;
        minutes = 0;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* print_minutes(void* pString) {
    pthread_mutex_lock(&lock);
    if(seconds > 59) {
        minutes++;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* print_seconds(void* pString) {
    pthread_mutex_lock(&lock);
    if(seconds == 59 && minutes == 59 && hours == 23){
        hours = 0;
        minutes = 0;
        seconds = -1;
    }
    seconds++;
    pthread_mutex_unlock(&lock);
    return 0;
}

int main() {
    pthread_t second_thread, minute_thread, hours_thread;
    
    printf("Enter the time in HH:MM:SS format.\n");
    scanf("%d:%d:%d", &hours, &minutes, &seconds);
    
    printf("HH:MM:SS\n");
    
    while(1) {
        sleep(1);
        
        pthread_create(&second_thread, NULL, print_seconds, NULL);
        pthread_join(second_thread, NULL);
        
        pthread_create(&minute_thread, NULL, print_minutes, NULL);
        pthread_join(minute_thread, NULL);
        
        pthread_create(&hours_thread, NULL, print_hour, NULL);
        pthread_join(hours_thread, NULL);
        
        printf("%d:%d:%d\n", hours, minutes, seconds);
    }
    
    return 0;
}
