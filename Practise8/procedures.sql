--  Procedure to insert new user by name and phone
-- If user already exists, update phone
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name VARCHAR(100),
    p_phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM phonebook
        WHERE first_name = p_name
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- Procedure to insert many users
-- Validates phone and returns incorrect data
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[],
    INOUT incorrect_data TEXT[] DEFAULT ARRAY[]::TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    -- Check if array sizes are equal
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names array and phones array must have the same length';
    END IF;

    -- Loop through arrays
    FOR i IN 1 .. array_length(p_names, 1) LOOP

        -- Phone validation:
        -- allows optional + and 10 to 15 digits
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN

            -- If user exists -> update
            IF EXISTS (
                SELECT 1
                FROM phonebook
                WHERE first_name = p_names[i]
            ) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE first_name = p_names[i];
            ELSE
                INSERT INTO phonebook(first_name, phone)
                VALUES (p_names[i], p_phones[i]);
            END IF;

        ELSE
            incorrect_data := array_append(
                incorrect_data,
                p_names[i] || ' - ' || p_phones[i]
            );
        END IF;

    END LOOP;
END;
$$;


-- Procedure to delete data by username or phone
CREATE OR REPLACE PROCEDURE delete_by_username_or_phone(
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value
       OR phone = p_value;
END;
$$;