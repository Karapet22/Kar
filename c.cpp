#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#include <winsock2.h>
#pragma comment(lib, "ws2_32.lib") 
#else
#include <arpa/inet.h>
#include <unistd.h>  
#endif

#define SERVER "127.0.0.1" 
#define BUFLEN 1024         
#define PORT 8888           


class UDPSocket {
protected:
    SOCKET s;  

public:
    static int WSAInit();  

    UDPSocket();           
    virtual ~UDPSocket(); 

    int SendDatagram(char* msg, unsigned int msglen, struct sockaddr* si_dest, unsigned int slen);  
    int RecvDatagram(char* buf, unsigned int buflen, struct sockaddr* si_dest, int* slen);          
};


int UDPSocket::WSAInit() {
    static unsigned int count = 0;
    if (count++) return 0;  

#ifdef _WIN32
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed. Error Code: %d\n", WSAGetLastError());
        return -1; 
    }
    printf("Winsock initialized.\n");
#endif 

    return 0;
}

UDPSocket::UDPSocket() {
    if (WSAInit() < 0) {
        printf("Failed to initialize Winsock.\n");
        exit(EXIT_FAILURE);
    }

    if ((s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == SOCKET_ERROR) {
        printf("socket() failed with error code: %d\n", WSAGetLastError());
        exit(EXIT_FAILURE);
    }
}

UDPSocket::~UDPSocket() {
#ifdef _WIN32
    closesocket(s);
    WSACleanup();
#else
    close(s);  
#endif
}

int UDPSocket::SendDatagram(char* msg, unsigned int msglen, struct sockaddr* si_dest, unsigned int slen) {
    if (sendto(s, msg, (int)msglen, 0, si_dest, slen) == SOCKET_ERROR) {
        printf("sendto() failed with error code: %d\n", WSAGetLastError());
        return -1;  
    }
    return 0;  
}

int UDPSocket::RecvDatagram(char* buf, unsigned int buflen, struct sockaddr* si_dest, int* slen) {
    if (recvfrom(s, buf, buflen, 0, si_dest, slen) == SOCKET_ERROR) {
        printf("recvfrom() failed with error code: %d\n", WSAGetLastError());
        return -1;  
    }
    return 0;  
}


class UDPServer : public UDPSocket {
private:
    unsigned short mServerPort; 
    struct sockaddr_in mServer;  

public:
    UDPServer(unsigned short serverport = 8888); 
    virtual ~UDPServer(); 

    void Start();  
};

UDPServer::UDPServer(unsigned short serverport) : UDPSocket(), mServerPort(serverport) {
    mServer.sin_family = AF_INET;
    mServer.sin_addr.s_addr = INADDR_ANY; 
    mServer.sin_port = htons(mServerPort);  
#ifdef _WIN32
    WSADATA wsaData;
    int wsaStartupResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (wsaStartupResult != 0) {
        printf("WSAStartup failed with error code: %d\n", wsaStartupResult);
        exit(EXIT_FAILURE);
    }
#endif

    if (bind(s, (struct sockaddr*)&mServer, sizeof(mServer)) == SOCKET_ERROR) {
        printf("Bind failed with error code: %d\n", WSAGetLastError());
        exit(EXIT_FAILURE);
    }
}

UDPServer::~UDPServer() {
#ifdef _WIN32
    closesocket(s);
    WSACleanup();
#else
    close(s); 
#endif
}

void UDPServer::Start() {
    struct sockaddr_in si_other;
    int slen = sizeof(si_other);
    char buf[BUFLEN];
    char msg[BUFLEN];

    while (1) {
        printf("Waiting for data...\n");
        memset(buf, '\0', BUFLEN);

        if (RecvDatagram(buf, BUFLEN, (struct sockaddr*)&si_other, &slen) == 0) {
            printf("Received message: %s\n", buf);
            printf("Enter response: ");
            gets_s(msg, BUFLEN);

            SendDatagram(msg, (int)strlen(msg), (struct sockaddr*)&si_other, slen);
        }
    }
}


int main() {
   
    int choice;
    printf("Enter 1 for server, 2 for client: ");
    scanf("%d", &choice);
    getchar();

    if (choice == 1) {
        UDPServer server(PORT);
        server.Start();
    } else if (choice == 2) {
        UDPSocket udpSocket;
        struct sockaddr_in si_other;
        char message[] = "Hello, UDP Server!";
        unsigned int slen = sizeof(si_other);

        memset((char*)&si_other, 0, sizeof(si_other));
        si_other.sin_family = AF_INET;
        si_other.sin_port = htons(PORT);
        si_other.sin_addr.s_addr = inet_addr(SERVER);

        udpSocket.SendDatagram(message, sizeof(message), (struct sockaddr*)&si_other, slen);

        char buffer[BUFLEN];
        udpSocket.RecvDatagram(buffer, BUFLEN, (struct sockaddr*)&si_other, &slen);

        printf("Received from server: %s\n", buffer);
    } else {
        printf("Invalid choice. Exiting...\n");
    }

    return 0;
}
