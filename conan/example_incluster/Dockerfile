FROM conanio/gcc7

ADD kubernetes-c /home/conan/kubernetes-c
WORKDIR /home/conan/kubernetes-c
RUN conan create . user/testing

ADD inside_list_pod /home/conan/inside_list_pod
WORKDIR /home/conan/inside_list_pod/build
RUN conan install .. && cmake .. && cmake --build .

RUN ls -lisa build
