drop table if exists collected;
drop table if exists movies;
drop table if exists users;

create table users (
  id integer primary key,
  user text unique not null
);

create table movies (
  id integer primary key,
  movie text unique not null
);

create table collected (
  id integer primary key,
  user integer references users not null,
  movie integer references movies not null
);
