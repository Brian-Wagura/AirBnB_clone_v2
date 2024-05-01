from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """
    A Database Storage engine

    Attributes:
         __engine (sqlalchemy.engine.Engine): The engine to connect to a database
         __session (sqlalchemy.orm.session.Session): The session to query the database
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a DBStorage object
        """
        from models.base_model import Base

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        if os.getenv("HBNB_ENV") != "test":
            self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """
        Query current database session and return all objects

        Args:
            cls (str): The class to query

        Returns:
            dict: A dictionary of objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if cls is None:
            objects = self.__session.query(
                BaseModel, User, State, City, Amenity, Place, Review
            ).all()
        else:
            objects = self.__session.query(cls).all()

        return {obj.to_dict()["__class__"] + "." + obj.id: obj for obj in objects}

    def new(self, obj):
        """
        Add the object to the current database session

        Args:
            obj (object): The object to add
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
