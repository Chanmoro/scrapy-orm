from orator.migrations import Migration


class CreatePagesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        # To set other type column,
        # See https://orator-orm.com/docs/0.9/schema_builder.html#adding-columns
        with self.schema.create('pages') as table:
            table.increments('id')
            table.string('url')
            table.string('title')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pages')
