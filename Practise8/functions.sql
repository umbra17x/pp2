-- 1. Function to search records by pattern
-- Searches by first_name, surname, or phone

CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE (
    id INT,
    first_name VARCHAR(100),
    surname VARCHAR(100),
    phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        pb.id,
        pb.first_name,
        pb.surname,
        pb.phone
    FROM phonebook pb
    WHERE pb.first_name ILIKE '%' || p_pattern || '%'
       OR pb.surname ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%';
END;
$$;


-- 2. Function to return records with pagination
CREATE OR REPLACE FUNCTION get_phonebook_page(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    first_name VARCHAR(100),
    surname VARCHAR(100),
    phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        pb.id,
        pb.first_name,
        pb.surname,
        pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$;