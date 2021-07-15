FROM conanio/gcc7

RUN git clone https://github.com/uncrustify/uncrustify.git
RUN cd uncrustify &&\
    mkdir build &&\
    cd build &&\
    cmake .. &&\
    make &&\
    sudo make install

COPY kubernetes-c /home/conan/kubernetes-c
WORKDIR /home/conan/kubernetes-c
RUN conan create . user/testing

RUN mkdir -p /home/conan/inside_list_pod/build
COPY inside_list_pod /home/conan/inside_list_pod
WORKDIR /home/conan/inside_list_pod/build
RUN conan install .. && cmake .. && cmake --build .
