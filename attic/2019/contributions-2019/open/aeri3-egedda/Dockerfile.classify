FROM archlinux/base

LABEL maintainer=emil.gedda@emilgedda.se

RUN pacman -Syu --noconfirm gcc git make diffutils python python-pip \
    && mkdir /parsers && pip install python-Levenshtein

RUN git clone -j8 --recurse-submodules https://github.com/EmilGedda/simdjson.git 

RUN cd simdjson                                 \
    && make    SANITIZE=1 checkfile -j8         \
    && install dropbox       /parsers/dropbox   \
    && install fastjson      /parsers/fastjson  \
    && install gason         /parsers/gason     \
    && install jsmn          /parsers/jsmn      \
    && install rapidjson-enc /parsers/rapid-enc \
    && install rapidjson     /parsers/rapid     \
    && install sajson        /parsers/sajson    \
    && install simdjson      /parsers/simdjson  \
    && install ultrajson     /parsers/ultrajson

RUN rm -rf simdjson

WORKDIR /proj
ENTRYPOINT python classify.py crashes bugs /parsers/*
