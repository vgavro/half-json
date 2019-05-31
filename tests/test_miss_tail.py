# coding=utf8

import random
import unittest

from half_json.core import clear


class TestMissTailCase(unittest.TestCase):

    # by json-generator
    line = '[{"_id":"5cf12ecfb7af6c84da64571b","index":0,"guid":"c2aedc2a-7303-42e2-b5a8-d58afca2149f","isActive":false,"balance":"$1,322.22","picture":"http://placehold.it/32x32","age":24,"eyeColor":"blue","name":{"first":"Gardner","last":"Ford"},"company":"IMAGINART","email":"gardner.ford@imaginart.net","phone":"+1 (874) 563-3237","address":"779 Cortelyou Road, Manchester, North Carolina, 939","about":"Ut dolore commodo qui nisi aliquip. Ad occaecat duis ipsum laborum magna cillum non mollit est eu. Non consectetur consectetur amet sunt reprehenderit tempor ex ea pariatur deserunt magna mollit sint in. Qui cupidatat ad eiusmod laborum ad consectetur elit ut. Quis dolore irure irure mollit aliquip laborum consectetur. Culpa do et id in in eu minim exercitation labore. Anim ex laboris nulla occaecat.","registered":"Saturday, May 18, 2019 3:55 PM","latitude":"-55.587817","longitude":"89.374875","tags":["irure","culpa","sint","sint","aliqua"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Malinda Estes"},{"id":1,"name":"Mueller Ryan"},{"id":2,"name":"Vilma Woods"}],"greeting":"Hello, Gardner! You have 6 unread messages.","favoriteFruit":"banana"},{"_id":"5cf12ecf5f6594406acaf90f","index":1,"guid":"eb7581e2-9471-4435-a689-7615f1324489","isActive":false,"balance":"$3,243.81","picture":"http://placehold.it/32x32","age":28,"eyeColor":"green","name":{"first":"Neva","last":"Frederick"},"company":"ACCRUEX","email":"neva.frederick@accruex.org","phone":"+1 (935) 521-3229","address":"935 Colby Court, Vallonia, Wisconsin, 9524","about":"Eiusmod dolor fugiat proident ex officia Lorem cupidatat cupidatat ut sunt minim. Sit incididunt reprehenderit cupidatat aliqua minim ad. Pariatur deserunt ad ad culpa veniam irure sint dolor quis pariatur eu laboris officia. Ad consequat voluptate cupidatat anim nulla elit veniam ex ipsum mollit. Pariatur est est excepteur laboris incididunt aliquip excepteur elit velit. Sint eu aliqua nulla dolore incididunt dolore nisi quis adipisicing est enim tempor.","registered":"Saturday, April 13, 2019 11:36 AM","latitude":"-29.541751","longitude":"-93.408621","tags":["laborum","eu","non","do","ut"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Ofelia Harmon"},{"id":1,"name":"Phillips Flowers"},{"id":2,"name":"Conner Walker"}],"greeting":"Hello, Neva! You have 8 unread messages.","favoriteFruit":"strawberry"},{"_id":"5cf12ecf20d50e3aa3590acb","index":2,"guid":"f150d306-8ca8-4791-9e99-912a75bb12a1","isActive":false,"balance":"$1,897.79","picture":"http://placehold.it/32x32","age":35,"eyeColor":"green","name":{"first":"Angelia","last":"Daniels"},"company":"DIGIGEN","email":"angelia.daniels@digigen.info","phone":"+1 (924) 451-2569","address":"628 Clymer Street, Whitmer, Delaware, 2210","about":"Enim adipisicing irure nisi nisi cillum voluptate ea commodo deserunt. Labore commodo ea culpa do esse cupidatat commodo consequat. Aliquip aliqua ut enim duis commodo dolore sint incididunt nulla excepteur. Occaecat labore consectetur occaecat ipsum id dolore dolor. Incididunt sint veniam ea dolore officia mollit dolore ullamco excepteur. Esse et esse nostrud aliquip exercitation Lorem. Laboris pariatur duis consectetur tempor reprehenderit ullamco pariatur sit deserunt sint non mollit eu.","registered":"Monday, August 6, 2018 2:54 AM","latitude":"-44.812364","longitude":"-40.811892","tags":["amet","consectetur","consequat","ex","elit"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Kline Delaney"},{"id":1,"name":"Agnes Patterson"},{"id":2,"name":"Donna Weeks"}],"greeting":"Hello, Angelia! You have 6 unread messages.","favoriteFruit":"apple"},{"_id":"5cf12ecf4eaebd02791a0a5d","index":3,"guid":"14fd69a4-6e19-4f46-a95f-ab99f144d383","isActive":false,"balance":"$1,647.55","picture":"http://placehold.it/32x32","age":30,"eyeColor":"green","name":{"first":"Aurelia","last":"Bentley"},"company":"ZYTREK","email":"aurelia.bentley@zytrek.tv","phone":"+1 (859) 530-2393","address":"582 Narrows Avenue, Riceville, Texas, 3979","about":"Sunt do aliquip voluptate sint pariatur adipisicing et. Irure voluptate ad voluptate anim aute ipsum laboris et. Culpa nostrud consequat in ex Lorem ex. Nostrud quis qui cupidatat occaecat incididunt aliqua elit aliqua anim labore voluptate sint consectetur ullamco. Eiusmod fugiat laborum sint velit eu do ex labore sunt labore exercitation voluptate ut aliquip.","registered":"Wednesday, October 24, 2018 10:08 AM","latitude":"-66.524116","longitude":"42.643245","tags":["aliquip","et","tempor","sit","in"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Tameka Whitfield"},{"id":1,"name":"Tessa Shepard"},{"id":2,"name":"Meyers Barr"}],"greeting":"Hello, Aurelia! You have 8 unread messages.","favoriteFruit":"strawberry"},{"_id":"5cf12ecf9508728e7da0a68f","index":4,"guid":"ee0a1b2e-da52-4b3b-a3d5-353495e6098e","isActive":false,"balance":"$3,847.46","picture":"http://placehold.it/32x32","age":40,"eyeColor":"brown","name":{"first":"Sutton","last":"Hess"},"company":"LUXURIA","email":"sutton.hess@luxuria.co.uk","phone":"+1 (928) 456-2632","address":"125 Vista Place, Charco, Indiana, 3164","about":"Deserunt ut ad proident aliqua ipsum laborum officia deserunt ea aliquip. In commodo est et esse sit mollit adipisicing veniam. Nulla eiusmod voluptate minim laborum laboris in dolore in est fugiat dolor exercitation officia. Non mollit tempor id eiusmod ex anim adipisicing qui ea ullamco et cupidatat. Aliquip irure nulla amet Lorem id eiusmod eu velit sit.","registered":"Thursday, March 19, 2015 6:39 PM","latitude":"-35.426884","longitude":"-133.613414","tags":["fugiat","dolore","nostrud","consectetur","anim"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Dorothea Dawson"},{"id":1,"name":"Compton Wilder"},{"id":2,"name":"Kelly Caldwell"}],"greeting":"Hello, Sutton! You have 10 unread messages.","favoriteFruit":"strawberry"},{"_id":"5cf12ecf7bde15b99bdf63b8","index":5,"guid":"fe862564-7ad7-4c8f-9a0d-005657883490","isActive":true,"balance":"$2,323.98","picture":"http://placehold.it/32x32","age":32,"eyeColor":"brown","name":{"first":"Goodman","last":"Spence"},"company":"UNIWORLD","email":"goodman.spence@uniworld.io","phone":"+1 (919) 463-3731","address":"878 High Street, Zortman, Virgin Islands, 9952","about":"Qui non velit nisi est cillum amet fugiat culpa ut anim aliqua nisi. Culpa aliquip eiusmod dolore proident deserunt minim sint officia do pariatur fugiat. Occaecat adipisicing eu esse non in consequat culpa amet fugiat aute sunt aliqua adipisicing proident. Voluptate ea duis pariatur exercitation. Irure officia consequat excepteur eu laborum occaecat amet ipsum laborum in nostrud eiusmod occaecat tempor. Ex amet culpa ipsum eiusmod adipisicing non anim ex veniam aute in ullamco ut.","registered":"Wednesday, January 10, 2018 3:37 PM","latitude":"68.089656","longitude":"29.601085","tags":["velit","ut","qui","Lorem","minim"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Hutchinson Finch"},{"id":1,"name":"Banks Winters"},{"id":2,"name":"Santana Cortez"}],"greeting":"Hello, Goodman! You have 7 unread messages.","favoriteFruit":"banana"},{"_id":"5cf12ecfc62579578b1bc759","index":6,"guid":"76ec16d9-a30f-471a-8c8b-31ea2fc37912","isActive":true,"balance":"$3,657.56","picture":"http://placehold.it/32x32","age":29,"eyeColor":"green","name":{"first":"Corinne","last":"Nguyen"},"company":"REALMO","email":"corinne.nguyen@realmo.name","phone":"+1 (800) 451-3183","address":"412 Beard Street, Kapowsin, New York, 836","about":"Qui fugiat sunt culpa consequat sint cillum veniam ullamco et aute ipsum. Sit ad tempor duis ex pariatur sint aliquip. Proident magna aliquip commodo sit quis. Officia occaecat officia voluptate sit exercitation occaecat qui anim. Excepteur mollit aute proident eu. Eu esse consectetur sunt laboris.","registered":"Friday, February 3, 2017 12:02 PM","latitude":"-38.812149","longitude":"47.887586","tags":["in","aliqua","aliqua","occaecat","id"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Celina Copeland"},{"id":1,"name":"Watson Santos"},{"id":2,"name":"Melba Olsen"}],"greeting":"Hello, Corinne! You have 8 unread messages.","favoriteFruit":"strawberry"},{"_id":"5cf12ecf223310f0f99c3d6e","index":7,"guid":"798e53fb-6590-4fc9-ba1b-cbb597e555de","isActive":false,"balance":"$2,244.77","picture":"http://placehold.it/32x32","age":30,"eyeColor":"green","name":{"first":"Rene","last":"Gillespie"},"company":"SCHOOLIO","email":"rene.gillespie@schoolio.us","phone":"+1 (828) 413-2911","address":"465 Ridgecrest Terrace, Joppa, Connecticut, 8512","about":"Do aliquip consequat nulla esse anim. Nulla cillum tempor labore excepteur voluptate reprehenderit amet. Nisi officia ea nisi fugiat mollit non eiusmod. Proident nulla ea sunt non quis dolor laboris magna cillum laborum eu. Sit nostrud eu enim consequat irure laborum duis et irure Lorem. Ipsum fugiat aliquip aute consequat est culpa sint cillum Lorem fugiat pariatur deserunt. Occaecat esse ea esse officia laborum.","registered":"Sunday, May 19, 2019 12:15 PM","latitude":"-65.435682","longitude":"137.573407","tags":["velit","voluptate","aliqua","consectetur","qui"],"range":[0,1,2,3,4,5,6,7,8,9],"friends":[{"id":0,"name":"Krystal Freeman"},{"id":1,"name":"Jenny Ruiz"},{"id":2,"name":"Heather Wood"}],"greeting":"Hello, Rene! You have 7 unread messages.","favoriteFruit":"banana"}]' # noqa

    def test_range_tail(self):
        for i in range(1000):
            tail = random.randint(1, len(self.line))
            ok, _ = clear(self.line[:tail])
            self.assertTrue(ok)
