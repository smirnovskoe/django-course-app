from . import models

EMAIL_MESSAGES = {
    models.Course.CourseStatus.START: "Ваш курс уже начался!",
    models.Course.CourseStatus.ENDED: "Ваш курс уже закончился!",
}
