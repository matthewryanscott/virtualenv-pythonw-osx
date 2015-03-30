/*
 * This wrapper program executes a python executable hidden inside an
 * application bundle inside the Python framework. This is needed to run
 * GUI code: some GUI API's don't work unless the program is inside an
 * application bundle.
 */
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <err.h>

static char Python[] = PYTHONWEXECUTABLE;

int main(int argc, char **argv) {
     char **a;
     a = malloc((argc + 3) * sizeof(char *));
     memcpy(a + 2, argv, argc * sizeof(char *));
     a[0] = "/usr/bin/arch";
     a[1] = sizeof(char *) == 4 ? "-i386" : "-x86_64";
     a[2] = Python;
     a[argc+2] = NULL;
     execv("/usr/bin/arch", a);
     err(1, "execv: %s", "arch");
     /* NOTREACHED */
}
