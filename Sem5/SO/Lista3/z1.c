#include <sys/types.h>
#include <sys/wait.h>

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define LEN(x) (sizeof (x) / sizeof *(x))
#define TIMEO  30

static void sigpoweroff(void);
static void sigreap(void);
static void sigreboot(void);
static void spawn(char *const []);

static struct {
	int sig;
	void (*handler)(void);
} sigmap[] = { //tutaj mamy mapowanie co robi handler przy otrzymaniu danego sygnału
	{ SIGUSR1, sigpoweroff }, //wylaczenie systemu
	{ SIGCHLD, sigreap     }, //grzebanie procesów zombie
	{ SIGALRM, sigreap     }, // ^^
	{ SIGINT,  sigreboot   }, //reboot
};

#include "config.h"

static sigset_t set;

int
main(void)
{
	int sig;
	size_t i;

	if (getpid() != 1)
		return 1;
	chdir("/"); //zmienia folder na główny
	sigfillset(&set);
	sigprocmask(SIG_BLOCK, &set, NULL); //zablokowanie odbierania sygnałów
	spawn(rcinitcmd); //tworzy proces i uruchamia polecenie startowe systemu       
    //static char *const rcinitcmd[]     = { "/bin/rc.init", NULL };
	while (1) {
		alarm(TIMEO); //funkcja alarm wysyła sygnał SIGALRM po upłynięciu x sekund, w tym przypadku 30, jeśli program otrzyma SIGALRM to sprawdza czy nie ma jakis procesów do pogrzebania, stanowi to rodzaj strażnika
		sigwait(&set, &sig); //proces jest usypainy i czeka na nadejsie jakiegokolwiek zablokowanego sygnału ze zbioru, jesli on nadejdzie funkcja sigwait obudzi program
		for (i = 0; i < LEN(sigmap); i++) { // po obudzeniu w zaleznosci od rodzaju sygnału wywołuje się odpowiednia funkcja 
			if (sigmap[i].sig == sig) {
				sigmap[i].handler();
				break;
			}
		}
	}
	/* not reachable */
	return 0;
}

static void
sigpoweroff(void)
{
	spawn(rcpoweroffcmd);
}

static void
sigreap(void)
{
	while (waitpid(-1, NULL, WNOHANG) > 0) // waitpid z -1 czeka na dowolny proces potomny, a flaga WNOHAND sprawia ze funkcja nie blokuje procesu, ponieważ nakazuje powrót funkcji jesli nie ma zadnego procesu potomnego
		;
	alarm(TIMEO);
}

static void
sigreboot(void)
{
	spawn(rcrebootcmd);
}

static void
spawn(char *const argv[])
{
	switch (fork()) { // klonujemy proces
	case 0:
		sigprocmask(SIG_UNBLOCK, &set, NULL); //odblokowujemy sygnały w procesie potomnym
		setsid(); //tworzymy nową sesje by odciąć proces od rodzica
		execvp(argv[0], argv); // wywołujemy exec
		perror("execvp");
		_exit(1);
	case -1:
		perror("fork");
	}
}