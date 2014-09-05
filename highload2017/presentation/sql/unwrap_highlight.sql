create type test as ("a" text, "b" text);
insert into test_jsonb
values('{"a": 1, "b": 2, "c": 3}');
select q.* from test_jsonb,
|\colorbox{RedOrange}{jsonb\_populate\_record}|(NULL::test, data) as q;
