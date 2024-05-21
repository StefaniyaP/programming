from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher = relationship('Discipline', back_populates='teachers_name')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    name_of_the_discipline = Column(String)
    discipline = relationship('EducationalPlan', back_populates='name_of_the_d')
    teachers_name = relationship('Teacher', back_populates='teacher')


class EducationalPlan(Base):
    __tablename__ = 'educational_plans'
    id = Column(Integer, primary_key=True)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
    name_of_the_plan = Column(String)
    name_of_the_d = relationship('Discipline', back_populates='discipline')


# создание бд
engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заполнение данными
discipline1 = Discipline(name_of_the_discipline="Алгебра")
discipline2 = Discipline(name_of_the_discipline="Физика")
discipline3 = Discipline(name_of_the_discipline='История')

teacher1 = Teacher(name="Иванов И.И.")
teacher2 = Teacher(name="Петров П.П.")
teacher3 = Teacher(name="Петров П.П.")

educational_plan1 = EducationalPlan(name_of_the_plan="План 1")
educational_plan2 = EducationalPlan(name_of_the_plan="План 2")
educational_plan3 = EducationalPlan(name_of_the_plan='План 3')

# Запросы

# вывод всех учителей и дисциплин
teachers_with_disciplines = session.query(Teacher, Discipline).filter(Teacher.id == Discipline.teacher_id).all()
for teacher, discipline in teachers_with_disciplines:
    print(f"Учитель: {teacher.name}, Дисциплина: {discipline.name_of_the_discipline}")

# вывод всех учебных планов и дисциплин, связанных с ними
educational_plans_with_disciplines = session.query(EducationalPlan, Discipline).filter(EducationalPlan.discipline_id == Discipline.id).all()
for educational_plan, discipline in educational_plans_with_disciplines:
    print(f"Учебный план: {educational_plan.name_of_the_plan}, Дисциплина: {discipline.name_of_the_discipline}")

# вывод всех учебных планов и связанных с ними учителей через дисциплины
educational_plans_with_teachers = session.query(EducationalPlan, Discipline, Teacher).filter(EducationalPlan.discipline_id == Discipline.id).filter(Discipline.teacher_id == Teacher.id).all()
for educational_plan, discipline, teacher in educational_plans_with_teachers:
    print(f"Учебный план: {educational_plan.name_of_the_plan}, Дисциплина: {discipline.name_of_the_discipline}, Учитель: {teacher.name}")

session.add(discipline1)
session.add(discipline2)
session.add(discipline3)
session.add(teacher1)
session.add(teacher2)
session.add(teacher3)
session.add(educational_plan1)
session.add(educational_plan2)
session.add(educational_plan3)
session.commit()
session.close()

