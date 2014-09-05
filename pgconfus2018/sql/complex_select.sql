SELECT
    st.data #>> '{item_a, another_item}' AS item_a,
    st.data #>> '{item_c}'               AS item_c,
    jsonb_array_elements(
        data #> '{item_b, subitem_a, subitem_b}'
    ) ->> 'some_key'                     AS item_e

    FROM some_table st LEFT JOIN another_table at
    ON (st.data #> '{item_b, key_a, key_b}') @>
        jsonb_build_array(jsonb_build_object(
            'key', 'some_key_name',
            'value', at.data #>> '{item_b, another_item}'
        ));
