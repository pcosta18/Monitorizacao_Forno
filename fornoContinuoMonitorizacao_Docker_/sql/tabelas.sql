
CREATE TABLE public.carbo_mes
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    carbo_temp_z1_mes real NOT NULL,
    carbo_temp_z2_mes real NOT NULL,
    carbo_temp_z3_mes real NOT NULL,
    carbo_temp_z4_mes real NOT NULL,
    carbo_temp_z5_mes real NOT NULL,
    azoto_n2_mes real NOT NULL,
    amoniaco_nh3_mes real NOT NULL,
    gas_ch4_mes real NOT NULL,
    metanol_ch3oh_mes real NOT NULL,
    o2_mes real NOT NULL,
    c_mes real NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE public.carbo_con
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    carbo_temp_z1_con real NOT NULL,
    carbo_temp_z2_con real NOT NULL,
    carbo_temp_z3_con real NOT NULL,
    carbo_temp_z4_con real NOT NULL,
    carbo_temp_z5_con real NOT NULL,
    azoto_n2_con real NOT NULL,
    amoniaco_nh3_con real NOT NULL,
    gas_ch4_con real NOT NULL,
    metanol_ch3oh_con real NOT NULL,
    PRIMARY KEY (id)
);



CREATE TABLE public.preox_mes
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    preox_temp_z1_mes real NOT NULL,
    preox_temp_z2_mes real NOT NULL,
    preox_temp_z3_mes real NOT NULL,
    PRIMARY KEY (id)
);




CREATE TABLE public.preox_con
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    preox_temp_z1_con real NOT NULL,
    preox_temp_z2_con real NOT NULL,
    preox_temp_z3_con real NOT NULL,
    PRIMARY KEY (id)
);



CREATE TABLE public.rev_mes
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    rev_temp_z1_mes real NOT NULL,
    rev_temp_z2_mes real NOT NULL,
    rev_temp_z3_mes real NOT NULL,
    rev_temp_z4_mes real NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.rev_con
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    rev_temp_z1_con real NOT NULL,
    rev_temp_z2_con real NOT NULL,
    rev_temp_z3_con real NOT NULL,
    rev_temp_z4_con real NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE public.tempera_mes
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    tempera_temp_mes real NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE public.tempera_con
(
    id bigserial NOT NULL,
    date date NOT NULL,
    time time(0) without time zone NOT NULL,
    tempera_temp_con real NOT NULL,
    PRIMARY KEY (id)
);