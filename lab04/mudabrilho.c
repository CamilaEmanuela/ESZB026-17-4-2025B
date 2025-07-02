/** Programa baseado no codigo disponibilizado em:
* Derek Molloy, Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux,
* Wiley 2016, ISBN 978-1-119-1868-1, http://www.exploringrpi.com/
*/
#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<termios.h>   // biblioteca para comunicacao serial

#include <wiringPi.h>
#include <softPwm.h>

int main(){
   int file, count;
   if ((file = open("/dev/ttyACM0", O_RDWR | O_NOCTTY | O_NDELAY))<0){
      perror("UART: Falha ao abrir o arquivo.\n");
      return -1;
   }
   struct termios options;             // cria estruturas para configurar a comunicacao
   tcgetattr(file, &options);          // ajusta os parametros do arquivo

   // Configura a comunicacao
   // 115200 baud, 8-bit, enable receiver, no modem control lines
   options.c_cflag = B115200 | CS8 | CREAD | CLOCAL;
   options.c_iflag = IGNPAR | ICRNL;   // ignora erros de paridade
   tcflush(file, TCIFLUSH);            // descarta informacao no arquivo
   tcsetattr(file, TCSANOW, &options); // aplica alteracoes imediatamente
   
   usleep(500000);
   
   int pino_PWM = 23;
   int range = 100;  
   wiringPiSetupGpio();                       // usar a numeracao GPIO, nao WPi
	pinMode(pino_PWM,OUTPUT);	           // configura GPIO23 como saida
   softPwmCreate(pino_PWM, 1, range);         // inicializa PWM por software

   unsigned char receive;         // cria um buffer para receber os dados
   while (1) {
      count = read(file, &receive, 1);
      if (count>0){
         printf("%d\n",receive);
         softPwmWrite (pino_PWM, receive); // altera o duty cycle do PWM
      }
      usleep (50000); 
   }
   close(file);
   return 0;
}
