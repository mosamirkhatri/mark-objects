class Query():
    CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS `marker`.`objects` (
        `id` INT NOT NULL,
        `image_name` VARCHAR(25) NOT NULL,
        `object_name` VARCHAR(25) NOT NULL,
        `x_min` INT NOT NULL,
        `y_min` INT NOT NULL,
        `x_max` INT NOT NULL,
        `y_max` INT NOT NULL,
        `timestamp` TIMESTAMP NULL DEFAULT NOW(),
        PRIMARY KEY (`id`));
    '''
    INSERT_OBJECTS = '''
        INSERT INTO objects (image_name, object_name, x_min, y_min, x_max, y_max) values (%s, %s, %s, %s, %s, %s);
        '''
    SELECT_OBJECTS = '''
        SELECT image_name, object_name, x_min, y_min, x_max, y_max, timestamp from objects where DATE(timestamp) >= %s AND DATE(timestamp) <= %s
    '''
