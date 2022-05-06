# ![HsqlDBembeddedOOo logo](img/HsqlDBembeddedOOo.png) HsqlDBembeddedOOo

**Ce [document](https://prrvchr.github.io/HsqlDBembeddedOOo/README_fr) en français.**

**The use of this software subjects you to our** [**Terms Of Use**](https://prrvchr.github.io/HsqlDBembeddedOOo/source/HsqlDBembeddedOOo/registration/TermsOfUse_en)

# version [0.0.4](https://prrvchr.github.io/HsqlDBembeddedOOo#historical)

## Introduction:

**HsqlDBembeddedOOo** is part of a [Suite](https://prrvchr.github.io/) of [LibreOffice](https://www.libreoffice.org/download/download/) and/or [OpenOffice](https://www.openoffice.org/download/index.html) extensions allowing to offer you innovative services in these office suites.  

This extension allows you:
- To overcome [bug 139538](https://bugs.documentfoundation.org/show_bug.cgi?id=139538) for users of **LibreOffice on Linux**.
- To use Embedded HsqlDB in uncompressed (split) mode, which is more robust, with the version of the HsqlDB driver of your choice.
- To migrate data from an embedded database (odb file) to the full feature HsqlDB driver: [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/), see: [How to migrate an embedded database](https://prrvchr.github.io/HsqlDBembeddedOOo/#how-to-migrate-an-embedded-database).

HsqlDBembeddedOOo only works in split mode, with the ability to extract (decompress) the data contained in an odb file when connecting if a folder with the same name and location as the odb file does not exist. This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice driver (Embedded HsqlDB).  
If these features do not concern you, then I recommend you to use the driver [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/) allowing to exploit all the functionalities offered by HsqlDB.

Being free software I encourage you:
- To duplicate its [source code](https://github.com/prrvchr/HsqlDBembeddedOOo/).
- To make changes, corrections, improvements.
- To open [issue](https://github.com/prrvchr/HsqlDBembeddedOOo/issues/new) if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

## Requirement:

[HsqlDB](http://hsqldb.org/) is a database written in Java.  
Its use requires the [installation and configuration](https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10) in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium](https://adoptium.net/releases.html?variant=openjdk11) as your Java installation source.

If you are using **LibreOffice on Linux**, then you are subject to [bug 139538](https://bugs.documentfoundation.org/show_bug.cgi?id=139538).  
To work around the problem, please uninstall the packages:
- libreoffice-sdbc-hsqldb
- libhsqldb1.8.0-java

OpenOffice and LibreOffice on Windows are not subject to this malfunction.

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install [HsqlDBembeddedOOo.oxt](https://github.com/prrvchr/HsqlDBembeddedOOo/raw/master/source/HsqlDBembeddedOOo/dist/HsqlDBembeddedOOo.oxt) extension version 0.0.4.

Restart LibreOffice / OpenOffice after installation.

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![HsqlDBembeddedOOo screenshot 1](img/HsqlDBembeddedOOo-1.png)

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded HsqlDB Driver
- click on button: Next

![HsqlDBembeddedOOo screenshot 2](img/HsqlDBembeddedOOo-2.png)

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![HsqlDBembeddedOOo screenshot 3](img/HsqlDBembeddedOOo-3.png)

Have fun...

### How to migrate an embedded database:

If you want to migrate an integrated database (HsqlDB version 1.8.0) to the latest version (for example 2.5.1), follow these steps:
- 1 - If it is not already installed, install this extension.
- 2 - Make a copy (backup) of your database (odb file).
- 3 - Open the odb file in Base (double click on the odb file).
- 4 - In Base go to: Tools -> SQL and type the SQL command: `SHUTDOWN COMPACT` or `SHUTDOWN SCRIPT`.
- 5 - Change the version of the HsqlDB driver in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver, with a version [2.4.0](https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.0/hsqldb-2.4.0.jar) or [2.4.1](https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.4.1/hsqldb-2.4.1.jar) or [2.5.0](https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.0/hsqldb-2.5.0.jar) (You must rename the jar file to hsqldb.jar for it to be taken into account).
- 6 - Restart LibreOffice / OpenOffice after changing the driver (hsqldb.jar).
- Repeat this procedure at step 3 using version [2.5.1](https://repo1.maven.org/maven2/org/hsqldb/hsqldb/2.5.1/hsqldb-2.5.1.jar).
- To finish, repeat step 3 then 4.

Now you can use the full feature version of the driver [HsqlDBDriverOOo](https://prrvchr.github.io/HsqlDBDriverOOo/), your database is in a folder with the same name and location as your odb file.

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

I encourage you in case of problem :-(  
to create an [issue](https://github.com/prrvchr/HsqlDBembeddedOOo/issues/new)  
I will try to solve it ;-)

## Historical:

### What has been done for version 0.0.1:

- The writing of this driver was facilitated by a [discussion with Villeroy](https://forum.openoffice.org/en/forum/viewtopic.php?f=13&t=103912), on the OpenOffice forum, which I would like to thank, because knowledge is only worth if it is shared...

- Using the old version of HsqlDB 1.8.0 (can be easily updated).

- Added a dialog box allowing to update the driver (hsqldb.jar) in: Tools -> Options -> Base drivers -> Embedded HsqlDB driver

- Many other fix...

### What has been done for version 0.0.2:

- Now the driver automatically splits an odb when opened... This allow conversion of odb files produced by the built-in LibreOffice / OpenOffice HsqlDB driver ;-)

- Many other fix...

### What has been done for version 0.0.3:

- I especially want to thank fredt at [hsqldb.org](http://hsqldb.org/) for:

    - His welcome for this project and his permission to use the HsqlDB logo in the extension.

    - The quality of its HsqlDB database.

- Now works with OpenOffice on Windows.

- When unzipping, a file name clash now displays a precise error.

- Now correctly handles spaces in filenames and paths.

- Many other fix...

### What has been done for version 0.0.4:

- Modification of [Driver.py](https://github.com/prrvchr/HsqlDBembeddedOOo/blob/master/source/HsqlDBembeddedOOo/Driver.py) in order to make possible the use of the Uno service: `com.sun.star.sdb.RowSet`.

- Many other fix...

### What remains to be done for version 0.0.4:

- Add new language for internationalization...

- Anything welcome...
