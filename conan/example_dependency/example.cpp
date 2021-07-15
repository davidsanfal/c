#include <config/kube_config.h>
#include <include/apiClient.h>
#include <api/CoreV1API.h>
#include <malloc.h>
#include <stdio.h>
#include <errno.h>

int main(int argc, char *argv[])
{
    char *basePath = NULL;
    sslConfig_t *sslConfig = NULL;
    list_t *apiKeys = NULL;
    int rc = load_kube_config(&basePath, &sslConfig, &apiKeys, NULL);   /* NULL means loading configuration from $HOME/.kube/config */
    if (rc != 0) {
        printf("Cannot load kubernetes configuration.\n");
        return 0;
    }
}
