from lunohod_details.common import AngularServo360, AngularServo90, AngularServo90Plus
from lunohod_details.impls.wheels import Wheels, VNH3SP30Motor
from lunohod_details.impls.bucket import Bucket
from lunohod_details.impls.claw import Claw
from lunohod_details.impls.hand import Hand


class Lunohod():
    def __init__(
        self,
        wheels: Wheels,
        hand_1: Hand,
        hand_2: Hand,
        bucket: Bucket,
        claw: Claw
    ) -> None:
        self.wheels = wheels
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.bucket = bucket
        self.claw = claw
