import json

partList = {}

partList["cpu"] = {"name":"Power Supply","description":'''<b>central processing unit</b> (CPU), also called a central processor, main processor or just processor, is the electronic circuitry within a computer that 
executes instructions that make up a computer program. The CPU performs basic arithmetic, logic, controlling, and input/output (I/O) operations specified by the instructions in 
the program. The computer industry used the term "central processing unit" as early as 1955.[1][2] Traditionally, the term "CPU" refers to a processor, more specifically to its 
processing unit and control unit (CU), distinguishing these core elements of a computer from external components such as main memory and I/O circuitry

The form, design, and implementation of CPUs have changed over the course of their history, but their fundamental operation remains almost unchanged. Principal 
components of a CPU include the arithmetic logic unit (ALU) that performs arithmetic and logic operations, processor registers that supply operands to the ALU and store the results
 of ALU operations, and a control unit that orchestrates the fetching (from memory) and execution of instructions by directing the coordinated operations of the ALU, registers and
  other components.

Most modern CPUs are microprocessors, where the CPU is contained on a single metal-oxide-semiconductor (MOS) integrated circuit (IC) chip. An IC that contains a CPU may also contain 
memory, peripheral interfaces, and other components of a computer; such integrated devices are variously called microcontrollers or systems on a chip (SoC). Some computers employ a
 multi-core processor, which is a single chip or "socket" containing two or more CPUs called "cores"
 '''}

partList["ram"] = {"name":"Power Supply","description":'''<b>Random-access memory</b> (RAM /ræm/) is a form of computer memory that can be read and changed in any order, typically used to store working data and machine 
code.[1][2] A random-access memory device allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory. 
In contrast, with other direct-access data storage media such as hard disks, CD-RWs, DVD-RWs and the older magnetic tapes and drum memory, the time required to read and write data 
items varies significantly depending on their physical locations on the recording medium, due to mechanical limitations such as media rotation speeds and arm movement.

RAM contains multiplexing and demultiplexing circuitry, to connect the data lines to the addressed storage for reading or writing the entry. Usually more than one bit of storage is 
accessed by the same address, and RAM devices often have multiple data lines and are said to be "8-bit" or "16-bit", etc. devices.
'''}

partList["hdd"] = {"name":"HDD","description":'''<b>A hard disk drive</b> (HDD), hard disk, hard drive, or fixed disk[b] is an electro-mechanical data storage device that uses magnetic storage to store and retrieve
 digital data using one or more rigid rapidly rotating platters coated with magnetic material. The platters are paired with magnetic heads, usually arranged on a moving actuator arm, 
 which read and write data to the platter surfaces.[2] Data is accessed in a random-access manner, meaning that individual blocks of data can be stored and retrieved in any order.
  HDDs are a type of non-volatile storage, retaining stored data even when powered off.[3][4][5]

Introduced by IBM in 1956,[6] HDDs were the dominant secondary storage device for general-purpose computers beginning in the early 1960s. HDDs maintained this position into the modern
 era of servers and personal computers, though personal computing devices produced in large volume, like cell phones and tablets, rely on flash products. More than 224 companies have 
 produced HDDs historically, though after extensive industry consolidation most units are manufactured by Seagate, Toshiba, and Western Digital. HDDs dominate the volume of storage produced
  (exabytes per year) for servers. Though production is growing slowly (by exabytes shipped[7]), sales revenues and unit shipments are declining because solid-state drives (SSDs) 
  have higher data-transfer rates, higher areal storage density, better reliability,[8] and much lower latency and access times
  '''
}

partList["ssd"] ={"name":"SSD","description": '''<b>A solid-state drive</b> (SSD) is a solid-state storage device that uses integrated circuit assemblies to store data persistently, typically using flash memory,
 and functioning as secondary storage in the hierarchy of computer storage. It is also sometimes called a solid-state device or a solid-state disk,[1] even though SSDs lack the physical
  spinning disks and movable read–write heads used in hard drives ("HDD") or floppy disks.[2]

Compared with the electromechanical drives, SSDs are typically more resistant to physical shock, run silently, and have quicker access time and lower latency.[3] SSDs store data in 
semiconductor cells. As of 2019, cells can contain between 1 and 4 bits of data. SSD storage devices vary in their properties according to the number of bits stored in each cell, with
 single-bit cells ("SLC") being generally the most reliable, durable, fast, and expensive type, compared with 2- and 3-bit cells ("MLC" and "TLC"), and finally quad-bit cells ("QLC") 
 being used for consumer devices that do not require such extreme properties and are the cheapest of the four. In addition, 3D XPoint memory (sold by Intel under the Optane brand), 
 stores data by changing the electrical resistance of cells instead of storing electrical charges in cells, and SSDs made from RAM can be used for high speed, when data persistence 
 after power loss is not required, or may use battery power to retain data when its usual power source is unavailable.[4] Hybrid drives or solid-state hybrid drives (SSHDs), such as 
 Apple's Fusion Drive, combine features of SSDs and HDDs in the same unit using both flash memory and a HDD in order to improve the performance of frequently-accessed data.[5][6][7]ensity,
  better reliability,[8] and much lower latency and access times

'''
}
partList["ps"] = {"name":"Power Supply","description":'''<b>A power supply unit</b> (or PSU) converts mains AC to low-voltage regulated DC power for the internal components of a computer. Modern personal computers universally
 use switched-mode power supplies. Some power supplies have a manual switch for selecting input voltage, while others automatically adapt to the mains voltage.

Most modern desktop personal computer power supplies conform to the ATX specification, which includes form factor and voltage tolerances. While an ATX power supply is connected to the mains
 supply, it always provides a 5 Volt standby (5VSB) voltage so that the standby functions on the computer and certain peripherals are powered. ATX power supplies are turned on and off by a
  signal from the motherboard. They also provide a signal to the motherboard to indicate when the DC voltages are in spec, so that the computer is able to safely power up and boot. 
  The most recent ATX PSU standard is version 2.31 as of mid-2008.
'''}

with open("parts.json","w") as file:
    json.dump(partList,file)