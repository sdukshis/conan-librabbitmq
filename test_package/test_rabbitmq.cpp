#include <amqp.h>
#include <amqp_tcp_socket.h>
#include <amqp_ssl_socket.h>
#include <amqp_framing.h>
#include <iostream>
int main(int argc, char const *argv[])
{
    amqp_connection_state_t conn = amqp_new_connection();

    std::cout << "Ok" << std::endl;
    return 0;
}